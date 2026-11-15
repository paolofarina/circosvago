"""Ritaglia le illustrazioni ad acquerello: toglie il fondo di carta della scansione
e lascia intorno al disegno un margine bianco irregolare, come un ritaglio fatto con le forbici.

Sorgenti: assets/img/illustrazioni/*.jpg (scansioni del cliente, fondo bianco/carta).
Uscita:   assets/img/illustrazioni/ritagli/<nome>.png (RGBA). I template le usano tramite il partial img.html,
          che le converte in WebP con trasparenza.

Il risultato è un'elaborazione delle illustrazioni del cliente (nessun disegno generato).

Uso:  python tools/ritaglia_illustrazioni.py
Poi, per la provenienza dei file (skill Impeccable):
      .claude/skills/impeccable/scripts/impeccable embed-prompt <file.png> --prompt "ORIGIN: ..."
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

RADICE = Path(__file__).resolve().parent.parent
SORGENTI = RADICE / "assets" / "img" / "illustrazioni"
USCITA = SORGENTI / "ritagli"

SOGLIA_CARTA = 228      # sopra questa luminosità minima (e poco saturo) è carta
# Immagini che arrivano già "a adesivo" (margine bianco e ombra grigia): soglia più bassa, così l'ombra resta fuori
SOGLIE_SPECIALI = {"corpo-e-movimento": 200}
SOGLIA_SATURAZIONE = 22
MARGINE = 0.012         # margine bianco delle forbici, in frazione del lato lungo
BORDO_SCANSIONE = 0.02  # striscia ai bordi della scansione considerata sempre carta
LATO_MAX = 1400         # le sorgenti in assets restano leggere: Hugo genera poi le misure WebP


def maschera_disegno(im: Image.Image, soglia: int = SOGLIA_CARTA) -> Image.Image:
    """Bianco dove c'è inchiostro o colore, nero dove c'è carta."""
    r, g, b = im.split()
    minimo = ImageChops.darker(ImageChops.darker(r, g), b)
    massimo = ImageChops.lighter(ImageChops.lighter(r, g), b)
    saturazione = ImageChops.subtract(massimo, minimo)
    scuro = minimo.point(lambda v: 255 if v < soglia else 0)
    colorato = saturazione.point(lambda v: 255 if v > SOGLIA_SATURAZIONE else 0)
    m = ImageChops.lighter(scuro, colorato)
    # via i puntini isolati della grana della carta
    m = m.filter(ImageFilter.MedianFilter(5))
    # i bordi della scansione (ombre del foglio) non fanno parte del disegno
    w, h = m.size
    b = int(max(w, h) * BORDO_SCANSIONE)
    nero = Image.new("L", (w, h), 0)
    nero.paste(m.crop((b, b, w - b, h - b)), (b, b))
    return nero


def ritaglia(src: Path, dest: Path) -> str:
    with Image.open(src) as im:
        im = im.convert("RGB")
        lato = max(im.size)
        disegno = maschera_disegno(im, SOGLIE_SPECIALI.get(src.stem, SOGLIA_CARTA))
        # margine delle forbici: allarga la sagoma, poi ammorbidisce e ri-soglia per un contorno irregolare ma pulito
        raggio = max(3, int(lato * MARGINE)) | 1
        sagoma = disegno.filter(ImageFilter.MaxFilter(raggio)).filter(ImageFilter.MaxFilter(raggio))
        sagoma = sagoma.filter(ImageFilter.GaussianBlur(raggio / 2)).point(lambda v: 255 if v > 90 else 0)
        sagoma = sagoma.filter(ImageFilter.GaussianBlur(1.2))  # antialias del bordo
        # dentro la sagoma: il disegno originale; nel margine: carta bianca pulita
        bianco = Image.new("RGB", im.size, (255, 255, 255))
        colore = Image.composite(im, bianco, disegno.filter(ImageFilter.MaxFilter(3)))
        out = colore.convert("RGBA")
        out.putalpha(sagoma)
        box = sagoma.point(lambda v: 255 if v > 8 else 0).getbbox()
        if box:
            out = out.crop(box)
        out.thumbnail((LATO_MAX, LATO_MAX), Image.Resampling.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest, optimize=True)
        return f"{out.width}x{out.height}"


def main() -> int:
    for src in sorted(SORGENTI.glob("*.jpg")):
        dest = USCITA / f"{src.stem}.png"
        print(f"{src.name} -> ritagli/{dest.name} ({ritaglia(src, dest)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
