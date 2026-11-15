"""Prepara le immagini del sito a partire dal materiale grezzo.

Legge tools/immagini.toml e per ogni voce:
- corregge la rotazione EXIF,
- ridimensiona il lato lungo a `max` px (default 2400),
- salva JPEG qualità 85 (o PNG ottimizzato per i .png),
- rimuove i metadati (posizione GPS inclusa).

Uso:  python tools/prepara_immagini.py [--forza]
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

from PIL import Image, ImageOps

RADICE = Path(__file__).resolve().parent.parent
SORGENTI = RADICE / "CIRCO SVAGO SITO"
MAPPA = RADICE / "tools" / "immagini.toml"
MAX_DEFAULT = 2400


def prepara(src: Path, dest: Path, lato_max: int, ritaglio: list[float] | None = None) -> str:
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if ritaglio:
            # ritaglio = [sinistra, alto, destra, basso] in frazioni dell'immagine (0–1),
            # poi si tolgono i bordi trasparenti rimasti
            w, h = im.size
            l, t, r, b = ritaglio
            im = im.crop((round(w * l), round(h * t), round(w * r), round(h * b)))
            if "A" in im.getbands() and (bbox := im.getchannel("A").getbbox()):
                im = im.crop(bbox)
        im.thumbnail((lato_max, lato_max), Image.Resampling.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.suffix.lower() == ".png":
            im.save(dest, optimize=True)
        else:
            if im.mode not in ("RGB", "L"):
                im = im.convert("RGB")
            im.save(dest, quality=85, optimize=True, progressive=True)
        return f"{im.width}x{im.height}"


def main() -> int:
    forza = "--forza" in sys.argv
    voci = tomllib.loads(MAPPA.read_text(encoding="utf-8"))["img"]
    errori = 0
    for v in voci:
        src = SORGENTI / v["src"]
        dest = RADICE / v["dest"]
        if not src.exists():
            print(f"MANCA   {v['src']}")
            errori += 1
            continue
        if not forza and dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
            print(f"ok      {v['dest']}")
            continue
        dim = prepara(src, dest, v.get("max", MAX_DEFAULT), v.get("ritaglio"))
        kb = dest.stat().st_size // 1024
        print(f"creata  {v['dest']}  ({dim}, {kb} KB)")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
