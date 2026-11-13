> **COPIA DI TEST — skill: Impeccable** (branch `test/impeccable`, anteprima su http://localhost:1314)
> In questa copia vale **BRIEF-TEST.md** (modalità "carta bianca"): `DESIGN.md` e `tokens.css` sono solo un riferimento,
> e `tools/controlla_design.py` non è obbligatorio. I vincoli non negoziabili del brief restano validi.
> Avvia l'anteprima con: `hugo server --port 1314`. Non modificare `C:\Progetti\circosvago` né le altre copie.

# Circo Svago — sito Hugo

Sito statico della scuola di circo Circo Svago (Albano Laziale). Hugo **extended** ≥ 0.146 (layout con la nuova struttura `layouts/_partials`, `layouts/_shortcodes`). Lingua: italiano.

## Regola principale

**Prima di toccare template, CSS o la struttura di una pagina, leggi `DESIGN.md`.** È vincolante.
- Colori, font e misure solo come variabili di `assets/css/tokens.css`.
- Si riusano i partial e gli shortcode esistenti (elenco in DESIGN.md §5) invece di scrivere HTML ad hoc.
- Un componente nuovo va aggiunto in tre punti: DESIGN.md, la pagina `/styleguide/` (`content/styleguide/index.md`) e il codice.
- Dopo ogni modifica lancia `python tools/controlla_design.py`: deve uscire senza errori.

## Comandi

```bash
hugo server              # anteprima su http://localhost:1313 (con le bozze: aggiungi -D)
hugo --minify            # build di produzione in public/
python tools/prepara_immagini.py   # ottimizza le foto da "CIRCO SVAGO SITO/" ai page bundle (vedi tools/immagini.toml)
python tools/controlla_design.py   # verifica i divieti di DESIGN.md
```

## Struttura

- `content/` — una cartella per pagina (page bundle: `index.md` + immagini). Le sezioni hanno `_index.md` con `colore:` (corallo | malva | blu).
- `layouts/` — `baseof.html`, `home.html`, `section.html`, `page.html`; componenti in `_partials/`, shortcode in `_shortcodes/`.
- `assets/css/` — `tokens.css` (token) + `main.css` (importa i file dei componenti in `assets/css/componenti/`).
- `assets/img/` — logo e illustrazioni condivise.
- `static/fonts/` — font self-hosted.
- `CIRCO SVAGO SITO/` — materiale grezzo del cliente. **Non modificarlo** e non pubblicarlo: Hugo lo ignora.
- `tools/` — script Python di supporto.

## Contenuti

- Front matter delle pagine: `title`, `description` (≤ 160 caratteri, per SEO e card), `copertina` (nome file nel bundle), `illustrazione` (opzionale, nome file in `assets/img/illustrazioni/`), `weight`.
- I testi mancanti si segnano con lo shortcode `{{< da-scrivere >}}…{{< /da-scrivere >}}`: non si inventano fatti (date, nomi, prezzi, orari).
- Tono: tu, frasi brevi, sentence case (DESIGN.md §7).
