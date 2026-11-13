"""Controlla che il codice rispetti i divieti di DESIGN.md.

Uso:  python tools/controlla_design.py
Esce con codice 1 se trova violazioni.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
TOKENS = RADICE / "assets" / "css" / "tokens.css"

# Eccezioni puntuali (file relativo, frammento della riga) con motivazione
ECCEZIONI = [
    ("layouts/_partials/head.html", "theme-color"),  # i meta tag non leggono variabili CSS
    # Texture del cartellone (DESIGN.md): bordo a zigzag e righe del quaderno sono gli unici gradienti ammessi
    ("assets/css/componenti/carta.css", "conic-gradient(from 135deg"),
    ("assets/css/componenti/carta.css", "linear-gradient(90deg, transparent 2.6rem"),
    ("assets/css/componenti/carta.css", "repeating-linear-gradient(to bottom"),
]

REGOLE_CSS = [
    (re.compile(r"#[0-9a-fA-F]{3,8}\b"), "colore esadecimale fuori da tokens.css"),
    (re.compile(r"\b(rgb|rgba|hsl|hsla)\(", re.I), "colore rgb()/hsl() fuori da tokens.css"),
    (re.compile(r"font-family\s*:(?!\s*(var\(|inherit))", re.I), "font-family senza token --f-*"),
    (re.compile(r"font-size\s*:(?!\s*(var\(|inherit))", re.I), "font-size senza token --t-*"),
    (re.compile(r"gradient\(", re.I), "gradiente (ammessi solo le texture in carta.css)"),
    (re.compile(r"@import\s+url\(\s*['\"]?https?:", re.I), "import da dominio esterno"),
]

REGOLE_HTML = [
    (re.compile(r"style=\"[^\"]*(#[0-9a-fA-F]{3,8}\b|rgb\(|hsl\()", re.I), "colore scritto a mano in style="),
    (re.compile(r"<(script|link)[^>]+(src|href)=\"https?://", re.I), "risorsa caricata da dominio esterno"),
    (re.compile(r"\b(jquery|bootstrap|swiper|slick|owl\.carousel)\b", re.I), "libreria esterna"),
    (re.compile(r"fonts\.googleapis|fonts\.gstatic", re.I), "Google Fonts remoto (GDPR)"),
]

IMG_CONSENTITI = {"layouts/_partials/img.html", "layouts/_partials/lightbox.html"}


def eccezione(rel: str, riga: str) -> bool:
    return any(rel == f and frammento in riga for f, frammento in ECCEZIONI)


def controlla() -> list[str]:
    errori: list[str] = []

    for css in sorted((RADICE / "assets" / "css").rglob("*.css")):
        if css == TOKENS:
            continue
        rel = css.relative_to(RADICE).as_posix()
        for n, riga in enumerate(css.read_text(encoding="utf-8").splitlines(), 1):
            codice = re.sub(r"/\*.*?\*/", "", riga)
            for regex, msg in REGOLE_CSS:
                if regex.search(codice) and not eccezione(rel, riga):
                    errori.append(f"{rel}:{n}  {msg}\n    {riga.strip()}")

    for html in sorted((RADICE / "layouts").rglob("*.html")):
        rel = html.relative_to(RADICE).as_posix()
        for n, riga in enumerate(html.read_text(encoding="utf-8").splitlines(), 1):
            if eccezione(rel, riga):
                continue
            for regex, msg in REGOLE_HTML:
                if regex.search(riga):
                    errori.append(f"{rel}:{n}  {msg}\n    {riga.strip()}")
            if "theme-color" not in riga and re.search(r"#[0-9a-fA-F]{6}\b", riga) and "href=\"#" not in riga:
                errori.append(f"{rel}:{n}  colore esadecimale in un template\n    {riga.strip()}")
            if re.search(r"<img\b", riga) and rel not in IMG_CONSENTITI:
                errori.append(f"{rel}:{n}  <img> diretto: usa il partial img.html\n    {riga.strip()}")

    for md in sorted((RADICE / "content").rglob("*.md")):
        rel = md.relative_to(RADICE).as_posix()
        testo = md.read_text(encoding="utf-8")
        if re.search(r"<img\b|<div\b|style=", testo):
            errori.append(f"{rel}  HTML nel contenuto: usa markdown o shortcode")

    return errori


def segnaposto() -> list[str]:
    trovati = []
    for md in sorted((RADICE / "content").rglob("*.md")):
        n = md.read_text(encoding="utf-8").count("{{< da-scrivere >}}")
        if n:
            trovati.append(f"{md.relative_to(RADICE).as_posix()} ({n})")
    return trovati


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    errori = controlla()
    for e in errori:
        print("✗", e)
    mancanti = segnaposto()
    if mancanti:
        print(f"\nℹ Segnaposto 'da-scrivere' ancora presenti in {len(mancanti)} pagine:")
        for m in mancanti:
            print("  -", m)
    print(f"\n{'✗ ' + str(len(errori)) + ' violazioni' if errori else '✓ Nessuna violazione di DESIGN.md'}")
    sys.exit(1 if errori else 0)
