"""Estrae dalla brochure 2025 (PDF) i piccoli disegni vettoriali e li salva come SVG puliti.

Ogni elemento è ricostruito solo dai tracciati vettoriali che stanno dentro il suo riquadro
(niente sfondo, niente testo, niente foto). I disegni a linee bianche della brochure diventano
`currentColor`, così nel sito prendono il colore dal CSS.

Uso:  python tools/estrai_elementi_brochure.py "<percorso>/Brochure Circosvago 2025 pagine singole.pdf"
Uscita: assets/img/elementi/<nome>.svg
"""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf

RADICE = Path(__file__).resolve().parent.parent
USCITA = RADICE / "assets" / "img" / "elementi"

# nome: (pagina, riquadro x0 y0 x1 y1 in punti PDF, linee bianche → currentColor, seqno minimo)
# Il seqno minimo esclude tracciati più vecchi che cadono nel riquadro ma nella brochure sono nascosti da una maschera.
ELEMENTI = {
    "birilli": (5, (12, 298, 108, 402), False, 600),
    "monociclo": (5, (328, 288, 408, 402), False),
    "giocoliere": (4, (148, 134, 228, 216), False),
    "biciclo": (1, (268, 292, 388, 400), True),
    "clave": (3, (22, 280, 108, 396), True),
}


def colore(rgb, linea_bianca: bool) -> str:
    if rgb is None:
        return "none"
    r, g, b = (round(c * 255) for c in rgb)
    if linea_bianca and min(r, g, b) > 235:
        return "currentColor"
    return f"#{r:02X}{g:02X}{b:02X}"


def percorso(items) -> str:
    d, ultimo = [], None
    for it in items:
        tipo = it[0]
        if tipo == "l":
            a, b = it[1], it[2]
            if ultimo is None or abs(a.x - ultimo.x) > 0.01 or abs(a.y - ultimo.y) > 0.01:
                d.append(f"M{a.x:.1f} {a.y:.1f}")
            d.append(f"L{b.x:.1f} {b.y:.1f}")
            ultimo = b
        elif tipo == "c":
            a, c1, c2, b = it[1], it[2], it[3], it[4]
            if ultimo is None or abs(a.x - ultimo.x) > 0.01 or abs(a.y - ultimo.y) > 0.01:
                d.append(f"M{a.x:.1f} {a.y:.1f}")
            d.append(f"C{c1.x:.1f} {c1.y:.1f} {c2.x:.1f} {c2.y:.1f} {b.x:.1f} {b.y:.1f}")
            ultimo = b
        elif tipo == "re":
            r = it[1]
            d.append(f"M{r.x0:.1f} {r.y0:.1f}H{r.x1:.1f}V{r.y1:.1f}H{r.x0:.1f}Z")
            ultimo = None
        elif tipo == "qu":
            q = it[1]
            d.append(f"M{q.ul.x:.1f} {q.ul.y:.1f}L{q.ur.x:.1f} {q.ur.y:.1f}L{q.lr.x:.1f} {q.lr.y:.1f}L{q.ll.x:.1f} {q.ll.y:.1f}Z")
            ultimo = None
    return "".join(d)


def estrai(doc, pagina: int, riquadro, linea_bianca: bool, seq_min: int = 0) -> str:
    zona = pymupdf.Rect(*riquadro)
    pezzi, unione = [], None
    for dr in doc[pagina].get_drawings():
        r = dr["rect"]
        if not zona.contains(r) or dr.get("seqno", 0) < seq_min:
            continue
        d = percorso(dr["items"])
        if not d:
            continue
        if dr.get("closePath"):
            d += "Z"
        attr = [f'd="{d}"']
        fill = colore(dr.get("fill"), linea_bianca)
        attr.append(f'fill="{fill}"')
        if fill != "none" and dr.get("even_odd"):
            attr.append('fill-rule="evenodd"')
        if dr.get("fill_opacity") not in (None, 1, 1.0) and fill != "none":
            attr.append(f'fill-opacity="{dr["fill_opacity"]:.1f}"')
        stroke = colore(dr.get("color"), linea_bianca)
        if stroke != "none" and dr.get("width"):
            attr += [f'stroke="{stroke}"', f'stroke-width="{dr["width"]:.1f}"',
                     'stroke-linecap="round"', 'stroke-linejoin="round"']
        pezzi.append(f"<path {' '.join(attr)}/>")
        unione = r if unione is None else unione | r
    if unione is None:
        raise SystemExit(f"nessun tracciato nel riquadro {riquadro} a pagina {pagina}")
    m = 1.5
    vb = f"{unione.x0 - m:.1f} {unione.y0 - m:.1f} {unione.width + 2 * m:.1f} {unione.height + 2 * m:.1f}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
            f'width="{(unione.width + 2 * m) * 4:.0f}" height="{(unione.height + 2 * m) * 4:.0f}">'
            "<!-- Disegno dalla brochure Circo Svago 2025, estratto da tools/estrai_elementi_brochure.py -->"
            + "".join(pezzi) + "</svg>\n")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    doc = pymupdf.open(sys.argv[1])
    USCITA.mkdir(parents=True, exist_ok=True)
    for nome, (pagina, riquadro, bianco, *resto) in ELEMENTI.items():
        svg = estrai(doc, pagina, riquadro, bianco, *resto)
        (USCITA / f"{nome}.svg").write_text(svg, encoding="utf-8")
        print(f"{nome}.svg  {len(svg) / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
