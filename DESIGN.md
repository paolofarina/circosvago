# Circo Svago — Design system

Questo documento è **vincolante**. Ogni modifica a layout, CSS o contenuti visivi del sito deve rispettarlo.
Se una regola non basta per un caso nuovo, si aggiorna prima questo file e poi il codice, mai il contrario.

La versione visiva e verificabile di queste regole è la pagina **/styleguide/** del sito (`hugo server` → http://localhost:1313/styleguide/).

---

## 1. Principi

1. **Gioco, non vetrina.** Il tono è quello della brochure 2025: colorato, fatto a mano, caldo. Mai corporate, mai "charity" generico.
2. **Le illustrazioni sono il marchio.** Le figure ad acquerello (trapezio, cerchio, giocoliere, swing, hip hop, balena) sono l'elemento più riconoscibile: vanno usate come protagoniste, non come decorazione minore.
3. **Le foto raccontano persone vere.** Foto di allievi ed eventi, mai stock.
4. **Colore a blocchi.** Come nelle pagine della brochure: grandi campiture piene di un solo colore per sezione, non sfumature né gradienti.
5. **Leggibile da tutti.** Famiglie, scuole, enti: testi chiari, contrasto AA, si naviga bene da telefono.

---

## 2. Colore

Tutti i colori sono definiti **solo** in `assets/css/tokens.css`. Nessun altro file CSS o template può contenere valori esadecimali, `rgb()` o `hsl()`: si usano sempre le variabili.

### 2.1 Colori base

| Token | Valore | Uso |
|---|---|---|
| `--c-inchiostro` | `#2A2238` | testo principale, footer |
| `--c-inchiostro-soft` | `#5A5068` | testo secondario, didascalie |
| `--c-carta` | `#FFF8EF` | sfondo pagina (crema caldo) |
| `--c-bianco` | `#FFFFFF` | card, testo su campiture scure |
| `--c-linea` | `#EADFD2` | bordi e separatori sottili |

### 2.2 Colori di sezione (dalla brochure)

Campiture piene per i blocchi. Il testo sopra è sempre **bianco** (contrasto ≥ 4.5:1 verificato).

| Token | Valore | Origine | Associato a |
|---|---|---|---|
| `--c-corallo` | `#C2513F` | pagina "Dai spazio alla tua passione" | Scuola di circo / corsi |
| `--c-malva` | `#9C4A8A` | pagina "Scopri Circo Svago" | Chi siamo / progetti sociali |
| `--c-blu` | `#3C68B0` | pagina "e i nostri progetti!" | Eventi e spettacoli |

Varianti chiare per sfondi di sezione morbidi (testo sopra: `--c-inchiostro`):
`--c-corallo-chiaro` `#FBE4DF` · `--c-malva-chiaro` `#F4E3EF` · `--c-blu-chiaro` `#E2ECF8` · `--c-giallo-chiaro` `#FFF2C2`

### 2.3 Colori accento (dal logo)

Solo per **dettagli decorativi**: puntini, sottolineature, bordo superiore delle card, schizzi. **Mai** come sfondo di un testo e mai per il testo corrente.

`--c-giallo` `#F2C200` · `--c-arancio` `#E5561A` · `--c-verde` `#92C11B` · `--c-ciano` `#0DB4D9` · `--c-viola` `#906CA8` · `--c-rosa` `#DA609E`

### 2.4 Regole di contrasto

- Testo corrente: solo `--c-inchiostro` su chiari, solo `--c-bianco` su corallo/malva/blu/inchiostro.
- Il giallo non porta mai testo bianco.
- Link nel testo: `--c-link` `#B04535` sottolineato (5.3:1 su carta, 4.6:1 sui fondi chiari). Il corallo pieno non va usato per testo su carta: fa 4.39:1.

Rapporti verificati (WCAG): bianco su corallo 4.62 · su malva 5.58 · su blu 5.53 · inchiostro su carta 14.4 · inchiostro-soft su carta 7.2 · inchiostro su giallo 9.0.

---

## 3. Tipografia

Tre famiglie, ognuna con **un solo ruolo**. I font sono self-hosted in `static/fonts/` (niente Google Fonts remoto: GDPR).

| Token | Famiglia | Ruolo | Regole |
|---|---|---|---|
| `--f-script` | Yellowtail | titoli "firma" (h1 di pagina, titolo di sezione in home) | mai sotto `--t-2xl`; mai in maiuscolo; max 6–7 parole |
| `--f-titolo` | Josefin Sans 600/700 | h2, h3, menu, bottoni, etichette | h2/h3 in sentence case; etichette e menu in MAIUSCOLO con `letter-spacing: .06em` |
| `--f-testo` | Nunito 400–800 | tutto il testo corrente | grassetto 700 per enfasi; corsivo solo per citazioni |

### Scala (fluida, `clamp`)

| Token | Mobile → Desktop | Uso |
|---|---|---|
| `--t-sm` | 0.875rem | didascalie, note |
| `--t-base` | 1.0625rem → 1.125rem | corpo |
| `--t-lg` | 1.25rem | lead, intro |
| `--t-xl` | 1.5rem → 1.75rem | h3 |
| `--t-2xl` | 1.875rem → 2.5rem | h2 |
| `--t-3xl` | 2.5rem → 4rem | h1 script |
| `--t-4xl` | 3rem → 5.5rem | solo hero home |

- Interlinea corpo 1.65, titoli 1.15.
- Larghezza massima del testo: `--w-testo` (68ch).

---

## 4. Spazi, forme, ombre

- **Spazi**: scala a base 4px, `--s-1` (4px) … `--s-10` (128px). Mai valori arbitrari.
- **Sezioni**: padding verticale `--s-sezione` (fluido 64 → 112px).
- **Contenitori**: `--w-max` 1200px, gutter laterale `--s-gutter` (16px mobile → 32px).
- **Raggi**: `--r-sm` 8px (input, tag) · `--r-md` 16px (immagini) · `--r-lg` 28px (card, blocchi) · `--r-pill` (bottoni).
- **Ombre**: solo `--ombra-1` (card a riposo) e `--ombra-2` (hover). Calde, mai grigio freddo.
- **Movimento**: transizioni `--durata` 200ms; animazioni disattivate con `prefers-reduced-motion`.

---

## 5. Componenti

Ogni componente esiste come partial o shortcode Hugo e ha una sezione nella styleguide. **Non si scrive HTML ad hoc nelle pagine** se esiste un componente.

| Componente | File | Note |
|---|---|---|
| Header + menu | `_partials/header.html` | logo a sinistra, menu a tendina su desktop, pannello a schermo intero su mobile |
| Hero home | `_partials/hero-home.html` | illustrazione balena + titolo script + tagline |
| Testata pagina | `_partials/testata.html` | campitura nel colore della sezione, titolo script bianco, illustrazione opzionale |
| Card | `_partials/card.html` | immagine 4:3, bordo superiore 6px in un colore accento a rotazione, titolo Josefin |
| Bottone | classi `.btn`, `.btn--pieno`, `.btn--bordo`, `.btn--chiaro` | pill, Josefin maiuscolo |
| Galleria | shortcode `{{</* galleria */>}}` | griglia di miniature, apertura in lightbox (`<dialog>`) |
| Nastro foto | `_partials/nastro.html` | carosello orizzontale scroll-snap, senza librerie |
| Elenco puntato | markdown normale | i pallini sono cerchi colorati a rotazione (colori accento) |
| Blocco contatti | `_partials/contatti.html` | email, telefono, social |
| Segnaposto | shortcode `{{</* da-scrivere */>}}` | box tratteggiato giallo per contenuti mancanti: ben visibile, da eliminare prima della pubblicazione |

### Colore per sezione

Ogni sezione dichiara il proprio colore nel front matter (`colore: corallo | malva | blu`) e testate, bottoni e dettagli lo ereditano tramite la variabile `--c-sezione`.

| Sezione | Colore |
|---|---|
| Chi siamo | malva |
| Scuola di circo | corallo |
| Eventi e feste | blu |
| Progetti | malva |
| Contatti | corallo |

---

## 6. Immagini

- Le immagini sorgenti stanno in `CIRCO SVAGO SITO/` e **non** vengono pubblicate così come sono.
- Si preparano con `python tools/prepara_immagini.py` (lato lungo massimo 2400px, rotazione EXIF corretta, nomi puliti) e finiscono nella cartella della pagina (page bundle).
- Nei template si mostrano **solo** tramite il partial `_partials/img.html`, che genera WebP responsive con `srcset` e `loading="lazy"`.
- Le illustrazioni hanno sfondo bianco: su sfondo carta si usano con `mix-blend-mode: multiply` (classe `.illustrazione`).
- Ogni immagine ha un testo `alt` descrittivo in italiano. Le illustrazioni decorative hanno `alt=""`.
- Rapporti: card 4:3, nastro 3:4 (verticale), testata libero.

---

## 7. Tono dei testi

- Si parla col **tu** al visitatore ("Scegli il tuo corso", "Festeggia con noi").
- Frasi brevi, verbi attivi. Niente burocratese.
- Titoli in sentence case. Il maiuscolo è solo per etichette e menu (lo fa il CSS, nei file si scrive normale).
- Nomi propri del progetto scritti sempre così: **Circo Svago**, **Circus Playground**, **Città Circenz(s)e**, **LabBOLLA**, **Re-Play**.

---

## 8. Divieti

- ❌ Colori, font o misure scritti a mano fuori da `tokens.css`.
- ❌ Gradienti, ombre nere, angoli vivi su card e immagini.
- ❌ Librerie JS/CSS esterne (jQuery, Bootstrap, slider): HTML, CSS e JS vanilla bastano.
- ❌ Risorse caricate da CDN o da domini terzi (font, script, mappe incorporate) senza consenso.
- ❌ Più di un titolo script per schermata.
- ❌ Testo sopra le foto senza un fondo pieno che garantisca il contrasto.

Il controllo automatico dei divieti si lancia con `python tools/controlla_design.py`.
