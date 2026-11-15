---
name: Circo Svago
description: Il cartellone di classe di una scuola di circo ad Albano Laziale, fatto di cartoncini, ritagli e pennarello.
colors:
  giallo: "#F1D06B"
  rosso: "#AD5344"
  malva: "#814675"
  blu: "#3D5E97"
  nero: "#2B2735"
  bianco: "#FFFFFF"
  inchiostro: "#2B2735"
  matita: "#55505F"
  link: "#A8402E"
  foglio: "#FFFFFF"
  righe: "#C9D8EE"
  margine: "#E7A0A0"
  postit: "#FFE58A"
  nastro: "rgb(244 236 214 / .78)"
  linea: "#E4DED3"
  arancio: "#E07F4F"
  verde: "#9BBF5A"
  ciano: "#4FAECB"
  rosa: "#D982AE"
  viola: "#957BAA"
typography:
  display:
    fontFamily: "Shantell Sans, Comic Sans MS, Segoe Print, cursive"
    fontSize: "clamp(2.5rem, 1.6rem + 4.2vw, 5rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Shantell Sans, Comic Sans MS, Segoe Print, cursive"
    fontSize: "clamp(1.875rem, 1.45rem + 2vw, 3rem)"
    fontWeight: 650
    lineHeight: 1.05
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Shantell Sans, Comic Sans MS, Segoe Print, cursive"
    fontSize: "clamp(1.375rem, 1.2rem + 0.8vw, 1.75rem)"
    fontWeight: 700
    lineHeight: 1.05
  didascalia:
    fontFamily: "Shantell Sans, Comic Sans MS, Segoe Print, cursive"
    fontSize: "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)"
    fontWeight: 600
    lineHeight: 1.3
  display-corsivo:
    fontFamily: "Style Script, Shantell Sans, cursive"
    fontSize: "clamp(3rem, 1.9rem + 5vw, 6rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0"
  headline-corsivo:
    fontFamily: "Style Script, Shantell Sans, cursive"
    fontSize: "clamp(2.25rem, 1.7rem + 2.4vw, 3.5rem)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "0"
  body:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.6
  lead:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.1875rem, 1.1rem + 0.4vw, 1.375rem)"
    fontWeight: 600
    lineHeight: 1.5
  label:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 700
    lineHeight: 1.3
rounded:
  sm: "3px"
  md: "4px"
  lg: "6px"
  pill: "999px"
spacing:
  s-1: "0.25rem"
  s-2: "0.5rem"
  s-3: "0.75rem"
  s-4: "1rem"
  s-5: "1.5rem"
  s-6: "2rem"
  s-7: "3rem"
  s-8: "4rem"
  s-9: "6rem"
  s-10: "8rem"
  sezione: "clamp(3.5rem, 2.5rem + 4.5vw, 7rem)"
  gutter: "clamp(1rem, 0.5rem + 2.2vw, 2.5rem)"
components:
  button-pieno:
    backgroundColor: "{colors.nero}"
    textColor: "{colors.bianco}"
    typography: "{typography.title}"
    rounded: "{rounded.sm}"
    padding: ".55em 1.15em .6em"
    height: "3.25rem"
  button-bordo:
    backgroundColor: "{colors.foglio}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.sm}"
    padding: ".55em 1.15em .6em"
    height: "3.25rem"
  button-chiaro:
    backgroundColor: "{colors.giallo}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.sm}"
    padding: ".55em 1.15em .6em"
    height: "3.25rem"
  button-tondo:
    backgroundColor: "{colors.giallo}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.pill}"
    size: "3rem"
  foglio:
    backgroundColor: "{colors.foglio}"
    textColor: "{colors.inchiostro}"
    padding: "clamp(1.5rem, 4vw, 3rem)"
  striscia:
    backgroundColor: "{colors.foglio}"
    textColor: "{colors.inchiostro}"
    padding: ".45em .8em .5em"
  postit:
    backgroundColor: "{colors.postit}"
    textColor: "{colors.inchiostro}"
    typography: "{typography.didascalia}"
    padding: "1.5rem"
    width: "min(100%, 22rem)"
  stampa:
    backgroundColor: "{colors.foglio}"
    padding: "clamp(.4rem, 1vw, .6rem)"
---

<!-- Riscritto da zero (scelta: OVERWRITE) a fine del redesign "carta bianca" della copia di test, dopo la build.
     La decisione di sovrascrivere il DESIGN.md precedente (Yellowtail/Josefin/Nunito, bottoni a pillola, fondo crema,
     divieto di gradienti) è stata presa dall'agente orchestratore in una prova non presidiata, perché il brief di test
     rende il vecchio DESIGN.md solo un riferimento: non è una conferma dell'utente. Tutti i valori sono ricavati dal
     codice consegnato (assets/css/tokens.css, base.css, componenti/*.css, layouts/). -->

# Design System: Circo Svago

Questo documento è **vincolante** per template, CSS e struttura delle pagine. Se una regola non basta per un caso nuovo, si aggiorna prima questo file e poi il codice.

## Overview

**Creative North Star: "Il cartellone di classe"**

Il sito è un cartellone fatto a mano dalla scuola. Ogni sezione è un cartoncino a tutta pagina di un solo colore pieno (giallo, nero dell'album, malva, bianco, rosso, blu) con il bordo superiore tagliato con le forbici a zigzag, che si sovrappone alla sezione prima. Sopra il cartoncino si incollano i materiali: fogli bianchi per il testo, strisce di foglio per le frasi brevi, ritagli degli acquerelli del cliente, foto stampate col bordo bianco, post-it gialli, nastro di carta, bollini adesivi. I titoli sono scritti a pennarello (Shantell Sans), il testo è stampato in un carattere leggibilissimo (Atkinson Hyperlegible Next).

Ogni pezzo incollato è appena storto (da -1.5° a +2°: ogni rotazione è `--storto × --k-storto`, con `--k-storto: .5`) e ha un'ombra corta di carta appoggiata. Il pezzo interattivo si "stacca" dal cartellone quando ci passi sopra o lo raggiungi con la tastiera: si raddrizza, si alza di qualche pixel, l'ombra si allunga. All'apertura della pagina i pezzi della testata si posano uno alla volta, una sola volta.

La densità è da cartellone, non da vetrina: pochi pezzi grandi per sezione, molto colore pieno attorno. Rifiuta l'hero con foto a tutto schermo e testo sopra, la griglia di card tutte uguali, il fondo crema con decorazioni sparse.

**Key Characteristics:**
- Un colore pieno per sezione, a tutta larghezza, mai due fondi nella stessa sezione.
- Tutto ciò che sta sopra il cartoncino è un materiale di carta riconoscibile, incollato e storto.
- Titoli a pennarello, testo in un sans ad alta leggibilità; niente terza famiglia (l'unica eccezione è il corsivo opzionale dei titoli, vedi The Titoli Rule).
- Ombre di carta incollata in tono inchiostro, mai nere né colorate.
- Un solo gesto di movimento firma: staccare un pezzo dal cartellone.

## Colors

Cartoncini saturi ma caldi presi dalla brochure e dal logo, su cui si incolla carta bianca; il testo è sempre pennarello nero-viola o bianco, mai un colore d'accento.

Tutti i colori esistono **solo** come variabili in `assets/css/tokens.css`. Nessun altro file CSS o template contiene valori esadecimali, `rgb()` o `hsl()` (unica eccezione: `<meta name="theme-color">` in `head.html`, che non può leggere variabili e ripete `--c-giallo`).

### Primary
- **Giallo cartellone** (`--c-giallo`): il cartoncino di apertura della home e della chiusura contatti, il menu mobile a tutto schermo, il bottone chiaro, i bollini delle frecce, l'anello di focus. È il colore della scuola.

### Secondary
- **Rosso corallo** (`--c-rosso`): cartoncino della scuola di circo e dei corsi; è il colore di sezione `corallo`.
- **Malva** (`--c-malva`): cartoncino di Chi siamo e dei progetti; colore di sezione `malva`.
- **Blu quaderno** (`--c-blu`): cartoncino degli eventi; colore di sezione `blu`.
- **Nero album** (`--c-nero`): il cartoncino nero dell'album fotografico (nastro foto, gallerie, footer), il bottone pieno, l'etichetta "Contatti" nel menu desktop.

### Tertiary
- **Bollini adesivi** (`--c-arancio`, `--c-verde`, `--c-ciano`, `--c-rosa`, `--c-viola`): i colori del logo. Solo decorazione (i pallini degli elenchi a rotazione), **mai testo e mai fondo di un testo**.

### Neutral
- **Inchiostro** (`--c-inchiostro`): pennarello nero, tutto il testo su carta chiara e su giallo.
- **Matita** (`--c-matita`): testo secondario su bianco (etichette dei recapiti, note delle sedi).
- **Rosso link** (`--c-link`): link nel testo corrente sui fogli bianchi.
- **Foglio** (`--c-foglio`): la carta bianca di fogli, strisce, stampe, header, sottomenu.
- **Righe e margine del quaderno** (`--c-righe`, `--c-margine`): solo per la texture del foglio a righe.
- **Post-it** (`--c-postit`): post-it dei contatti e segnaposto `da-scrivere`.
- **Nastro** (`--c-nastro`): pezzetti di nastro di carta semitrasparente.
- **Linea** (`--c-linea`): bordi dei campi dei moduli e segnaposto delle immagini mancanti.

Le varianti chiare (`--c-corallo-chiaro`, `--c-malva-chiaro`, `--c-blu-chiaro`, `--c-giallo-chiaro`) e gli alias `--c-corallo`, `--c-carta`, `--c-inchiostro-soft` restano solo per le pagine non ancora ridisegnate e per l'hover del sottomenu: non si usano per superfici nuove.

### Contrasto misurato (WCAG, dai commenti di tokens.css)

| Coppia | Rapporto |
|---|---|
| inchiostro su giallo | 9.7:1 |
| bianco su rosso | 5.1:1 |
| bianco su malva | 6.8:1 |
| bianco su blu | 6.5:1 |
| bianco su nero (e inchiostro su bianco) | 14.5:1 |
| matita su bianco | 7.8:1 |
| link su foglio bianco | 6.1:1 |

**The Un Cartoncino Rule.** Ogni sezione è un solo cartoncino pieno con il suo testo fisso: inchiostro su giallo e bianco, bianco su rosso, malva, blu e nero. Sui cartoncini scuri i link nudi diventano bianchi; sulla carta chiara incollata sopra (foglio, striscia, post-it) torna l'inchiostro o il rosso link.

**The Bollino Rule.** I cinque colori del logo sono adesivi: decorano, non portano mai testo.

**The Pagina di Sezione Rule.** Una pagina di sezione (scuola, eventi, progetti, chi siamo) non apre mai con un cartoncino muto a tutto schermo. La testata ha sempre due azioni (`azione_elenco`, che porta all'elenco con una freccia in giù, e "Scrivici"). Su telefono l'illustrazione sola sta accanto al titolo, piccola, così il primo schermo mostra l'inizio della sezione successiva. Con `elenco_in_alto: true` l'elenco delle pagine viene subito dopo la testata, prima del testo; con 5 pagine la griglia ne mette 5 su una riga (`griglia-card--n5`), mai una scheda orfana.

**The Colore di Sezione Rule.** Una sezione del sito dichiara `colore: corallo | malva | blu` nel front matter di `_index.md`; `_partials/colore.html` lo eredita risalendo le pagine e `_partials/carta-sezione.html` lo traduce nel cartoncino (`corallo → rosso`, `malva → malva`, `blu → blu`). Testata e sezione "altro" usano quel cartoncino.

## Typography

**Display Font:** Shantell Sans (con Comic Sans MS, Segoe Print, cursive)
**Body Font:** Atkinson Hyperlegible Next (con Segoe UI, system-ui, sans-serif)

**Character:** un pennarello vero e un testo stampato chiarissimo: il primo dà la mano della scuola, il secondo garantisce che famiglie e scuole leggano tutto da telefono. Entrambi variabili, self-hosted in `static/fonts/` (latin, woff2, `font-display: swap`).

### Hierarchy
- **Display** (Shantell `--w-display` 700, `--t-4xl` fino a 5rem, interlinea 0.95, -0.025em): solo il titolo dell'apertura home e delle testate di pagina.
- **Headline** (Shantell; h1 a `--w-display` 700 in `--f-firma`, h2 a `--w-titolo` 650; `--t-3xl` per h1 e titoli di chiusura, `--t-2xl` per h2 di sezione; interlinea 1.05, -0.01em, `text-wrap: balance`): titoli di sezione, larghezza massima 22ch.
- **Title** (Shantell 700, `--t-xl`): h3, titoli di card e dei pezzi piccoli; `--t-lg` per h4, titolo del post-it, nomi dei corsi, bottoni.
- **Didascalia a pennarello** (Shantell 600, `--t-base`, interlinea 1.3): didascalie delle stampe e della lightbox, voci del post-it.
- **Body** (Atkinson 400, `--t-base`, interlinea 1.6, `text-wrap: pretty`): testo corrente, larghezza `--w-testo` (66ch).
- **Lead** (Atkinson 600, `--t-lg`, interlinea 1.5): la frase sotto il titolo, sempre su una striscia di foglio; massimo 30–34ch.
- **Label** (Atkinson 700, `--t-sm`, interlinea 1.3): etichette dei recapiti e del segnaposto. Sentence case, niente maiuscolo né spaziatura larga.

Scala fluida in `tokens.css` (`--t-sm` … `--t-4xl`); grandezze fuori scala solo come token dedicati e annotati (`--t-nav` per le voci del menu desktop, `--t-frase` per il titolo-frase lungo dell'incipit).

**The Due Mani Rule.** Il pennarello scrive titoli, nomi, didascalie e bottoni; il testo da leggere è sempre Atkinson. Nessuna terza famiglia (salvo il corsivo opzionale della Titoli Rule), nessun font di sistema per i titoli.

**The Sentence Case Rule.** Titoli, bottoni, menu ed etichette si scrivono in sentence case; il sito non usa maiuscolo decorativo.

## Layout

- **Contenitore:** `--w-max` 78rem centrato, gutter laterale `--s-gutter` (fluido 1rem → 2.5rem).
- **Sezioni:** ogni sezione è un cartoncino a tutta larghezza; padding verticale `--s-sezione` (fluido 3.5rem → 7rem). Il bordo a zigzag (`--zigzag` 9px di passo) sporge sopra e morde la sezione precedente.
- **Spazi:** scala a base 4px, `--s-1` (4px) … `--s-10` (128px). Mai valori arbitrari.
- **Apertura e testate:** su telefono colonna unica testo → post-it → immagine; da 64rem due colonne (testo e post-it a sinistra, ritaglio o pila foto+ritaglio a destra). Il post-it con telefono ed email è sempre nel primo schermo.
- **Composizioni a pezzi diseguali:** "Cosa facciamo" è un pezzo grande più due piccoli (foto accanto al testo a ogni larghezza; da 56rem il grande occupa due righe); la serie dei corsi è una fila di ritagli (2 → 3 → 5 colonne, i pari scalati in basso da 72rem); la galleria è un collage a righe giustificate in cui ogni foto conserva le sue proporzioni.
- **Scorrimento laterale:** nastro foto e, sotto i 40rem, le quattro proposte eventi scorrono di lato con scroll-snap, invece di impilarsi.
- **Breakpoint usati:** 40rem, 48rem, 56rem, 64rem (menu desktop), 72rem, 78rem.
- **Header:** striscia di foglio bianco sticky, alta `--h-header` (4.75rem).

## Elevation & Depth

La profondità è carta incollata su carta: ombre corte offset + sfocatura nel tono dell'inchiostro (`--ombra-colore` 43 39 53, il tono di `--c-nero`), più la rotazione leggera di ogni pezzo. Niente ombre nere, niente ombre colorate, niente ombre dure senza sfocatura. I ritagli non hanno ombra rettangolare: `filter: drop-shadow` segue la sagoma.

### Shadow Vocabulary
- **Incollato** (`--ombra-1`): fogli, strisce, stampe, bottoni e blocchi a riposo.
- **Staccato** (`--ombra-2`): stato hover/focus dei pezzi staccabili, sottomenu, lightbox.
- **Post-it** (`--ombra-postit`): post-it e segnaposto, con la coda lunga della carta che si arriccia.
- **Nastro** (`--ombra-nastro`), **Bollino** (`--ombra-bollino`), **Header** (`--ombra-header`).
- **Posa** (`--ombra-posa`): solo nel primo fotogramma dell'animazione di apertura.
- **Ritaglio / ritaglio su** (`--ombra-ritaglio`, `--ombra-ritaglio-su`): drop-shadow a due strati che segue il contorno dell'acquerello.

**The Carta Incollata Rule.** Un pezzo a riposo ha sempre `--ombra-1` (o la sua variante di materiale) e una rotazione `--storto`; solo nello stato staccato si raddrizza e prende `--ombra-2`.

## Shapes

Carta tagliata: angoli vivi o appena smussati (`--r-sm` 3px su bottoni e menu; `--r-md`/`--r-lg` disponibili), mai arrotondati morbidi su card, foto e fogli. Le sole forme tonde sono gli adesivi: bollini degli elenchi, bottoni tondi, icone social (`50%`), e il fumetto della citazione (raggio 1.5rem con la codina). Il bordo superiore delle sezioni è tagliato a zigzag. Le stampe hanno il bordo bianco; i ritagli hanno il margine bianco attorno alla sagoma, generato da `tools/ritaglia_illustrazioni.py`.

**The Sobrietà Rule.** Versione sobria (novembre 2026): cartoncini ammorbiditi (~25% meno saturi), ombre più corte, titoli 700/650 invece di 800, inclinazioni dimezzate con un solo token (`--k-storto`), nastro adesivo solo sui pezzi principali (apertura, foto di testata, fogli di testo, foglio dei contatti), mai su ogni foto di una serie.

**The Elementi Rule.** I piccoli disegni vettoriali della brochure 2025 stanno in `assets/img/elementi/` (estratti con `tools/estrai_elementi_brochure.py`) e si inseriscono solo con `_partials/elemento.html`: birilli (footer), monociclo (chiusura contatti, da 56rem), giocoliere (testata di Circus Playground, via front matter `elemento:`), biciclo e clave a linee (accanto ai titoli dei corsi e degli eventi in home, colorati dal cartoncino via `mask`). Al massimo un elemento per sezione; sono decorativi (`alt=""`, `aria-hidden`).

**The Titoli Rule.** I titoli grandi usano `--f-firma`: Shantell Sans (pennarello) di default. `params.titoli = "corsivo"` in `hugo.toml` li passa a Style Script, il corsivo gratuito più vicino a quello della brochure (che è un monolineare commerciale non identificato): vale solo per titoli d'apertura, testate e titoli di sezione, mai per etichette, bottoni e post-it.

**The Texture Rule.** Gli unici gradienti ammessi sono le due texture del cartellone in `componenti/carta.css`: il bordo a zigzag (`conic-gradient`) e le righe e il margine del foglio di quaderno (`linear-gradient` + `repeating-linear-gradient`). Nessun altro gradiente, in nessun file (lo verifica `tools/controlla_design.py`).

## Components

Ogni componente esiste come partial, shortcode o classe di materiale; non si scrive HTML ad hoc nelle pagine se esiste un componente.

### Materiali (`assets/css/componenti/carta.css`)
- **Cartoncino** (`.cartoncino[data-carta="giallo|rosso|malva|blu|nero|bianco"]`, `--zigzag` per il bordo): ogni sezione. Imposta `--carta` e `--su-carta`.
- **Foglio** (`.foglio`, `.foglio--righe`): carta bianca per il testo lungo; il quaderno a righe allinea padding, paragrafi e citazioni a multipli della riga (1.75rem).
- **Striscia** (`.striscia`): un ritaglio di foglio largo quanto la frase (lead delle testate, nomi dei corsi).
- **Stampa** (`.stampa`): foto col bordo bianco, didascalia a pennarello sotto, attaccata a ciò che nomina.
- **Ritaglio** (`.ritaglio`): acquerello del cliente scontornato, con ombra sulla sagoma.
- **Post-it** (`.postit`): recapiti veloci a pennarello.
- **Nastro** (`.nastrato`, `.nastrato--angoli`): pezzetto di nastro in alto al centro o sugli angoli.

### Buttons
- **Shape:** etichetta di cartoncino incollata, angoli appena smussati (`--r-sm`), altezza minima 3.25rem, Shantell 700 `--t-lg`, ruotata di circa -1°.
- **Pieno** (cartoncino nero, testo bianco): la scelta principale.
- **Bordo** (foglio bianco, testo inchiostro, ruotato dall'altra parte): la scelta secondaria.
- **Chiaro** (giallo, testo inchiostro): l'azione principale sui cartoncini scuri.
- **Hover / Focus:** si raddrizza, sale di 3px, `--ombra-2`; la freccia a mano avanza di 4px. Al focus da tastiera si aggiunge l'anello giallo di 6px. `:active` torna giù.
- **Tondo** (`.btn-tondo`): bollino giallo 3rem per le frecce del nastro; disabilitato diventa un cerchio tratteggiato giallo.
- Shortcode `{{</* bottone link="…" stile="pieno|bordo" */>}}` per i contenuti.

### Cards / Containers
- **Card** (`_partials/card.html`): foto stampata con nastro (o ritaglio, se la pagina ha solo l'illustrazione), titolo a pennarello sotto; rotazioni a rotazione di 3. Tutta la card è cliccabile dal link del titolo. Se la sezione madre ha `schede_illustrate: true` (la scuola) la card mostra sempre il ritaglio ad acquerello del corso: **i corsi si presentano solo con i fumetti**, mai con un misto di foto e fumetti. La foto resta nella pagina del corso.
- **Blocco** (`.blocco`, solo home "Cosa facciamo"): pezzo di cartoncino del colore della sezione di destinazione con la foto che sborda.
- **Corsi** (`_partials/corsi.html`): la serie dei ritagli con il nome su una striscia; se un corso non ha illustrazione si usa la foto nella stessa cornice 1:2, mai un disegno inventato.

### Inputs / Fields
- **Stile** (solo pagina contatti, non ancora ridisegnata): bordo 2px `--c-linea`, `--r-sm`, fondo bianco. Al focus il bordo diventa blu.

### Navigation
- **Logo nell'header:** da 64rem in su il logo intero, ingrandito (11.25rem), dentro una finestra di carta alta 3.75rem che mostra solo la fascia centrale "CIRCO SVAGO – scuola di circo". Al passaggio o al focus la finestra scende come una linguetta sopra la pagina, senza spostare il contenuto. Il logo intanto si rimpicciolisce (8.25rem) e se ne vede l'85%. I parametri sono variabili in `header.css` (`--finestra`, `--centro`, `--aperta`, `--logo-l-aperto`). Sotto i 64rem c'è il logo tondo intero, senza finestra. Il logo non si ritaglia mai come file.
- **Desktop (≥ 64rem):** voci a pennarello su striscia bianca sticky; hover e pagina corrente sono un tratto di evidenziatore giallo storto che si allunga da sinistra. Sottomenu: foglio bianco storto con nastro, `--ombra-2`. L'ultima voce, Contatti, è un'etichetta nera sempre visibile.
- **Mobile:** bottone "Menu" nero; il menu è un cartoncino giallo a tutto schermo con voci grandi separate da righe, sottomenu su foglio, e il post-it dei contatti in fondo.
- **Briciole:** in testata, sopra il titolo, piccole e in grassetto, separate da "/".

### Focus da tastiera
Ovunque: contorno inchiostro 3px con offset 3px più anello giallo di 6px (`box-shadow`). Sui cartoncini scuri (rosso, malva, blu, nero) il contorno diventa giallo. I pezzi staccabili e i bottoni al focus si staccano come all'hover e tengono l'anello giallo; card e corsi spostano il segno sul titolo.

### Movimento
- **Curva e durata:** `--curva` (ease-out esponenziale) e `--durata` 220ms per tutte le transizioni di stato.
- **Staccare** (`.staccabile`): hover (solo dispositivi con hover) e focus → `rotate: 0`, `translate: 0 -6px`, `--ombra-2` (o `--ombra-ritaglio-su` per i ritagli).
- **Posare** (`.si-posa`, `--ordine`): una sola animazione d'ingresso per i pezzi della testata, 700ms, 110ms di scarto tra un pezzo e l'altro, attiva solo in `prefers-reduced-motion: no-preference`. Con `reduce` ogni animazione e transizione è azzerata.

### Partial e shortcode

| Componente | File | Scopo |
|---|---|---|
| Testata | `_partials/testata.html` | cartoncino di sezione, briciole, titolo display, lead su striscia, pila foto+ritaglio, post-it; nelle pagine di sezione due azioni (`azione_elenco` ↓ verso `#elenco`, "Scrivici" verso `#contatti`) |
| Post-it contatti | `_partials/biglietto.html` | telefono e email giusti (`tipo: corsi | eventi`) nel primo schermo |
| Chiusura contatti | `_partials/contatti.html` | cartoncino giallo `#contatti` con foglio dei recapiti, in fondo a ogni pagina |
| Corsi | `_partials/corsi.html` | serie dei ritagli dei corsi |
| Card | `_partials/card.html` | stampa o ritaglio + titolo |
| Galleria | `_partials/galleria.html`, shortcode `galleria` | collage di stampe con lightbox (`_partials/lightbox.html`, `<dialog>`) |
| Header / footer | `_partials/header.html`, `_partials/footer.html` | striscia bianca con menu; cartoncino nero con motto giallo |
| Freccia | `_partials/freccia.html` | freccia disegnata a mano, SVG inline decorativo |
| Colore di sezione | `_partials/colore.html`, `_partials/carta-sezione.html` | `colore` del front matter → cartoncino |
| Illustrazione | `_partials/illustrazione.html` | trova l'acquerello: preferisce il ritaglio PNG in `assets/img/illustrazioni/ritagli/`, altrimenti la scansione |
| Copertina | `_partials/copertina.html` | immagine di copertina della pagina (foto del bundle o illustrazione) |
| Immagine | `_partials/img.html` | **unico** modo di mostrare un raster: WebP responsive, `srcset`, lazy salvo `eager` |
| Segnaposto | `_partials/da-scrivere.html`, shortcode `da-scrivere` | post-it "Da scrivere" per i testi mancanti |
| Bottone | shortcode `bottone` | `.btn` nei contenuti markdown |

## Do's and Don'ts

### Do:
- **Do** usare colori, font, misure, ombre e durate solo come variabili di `assets/css/tokens.css`.
- **Do** dare a ogni sezione un solo cartoncino (`.cartoncino[data-carta]`) e, dopo la prima, il bordo a zigzag.
- **Do** mettere il testo lungo su un foglio, le frasi brevi su una striscia, i recapiti su un post-it: mai testo direttamente sopra una foto.
- **Do** ruotare ogni pezzo incollato con `calc(var(--storto) * var(--k-storto))` (effetto da -1.5° a +2°) e alternare il verso tra pezzi vicini.
- **Do** mostrare ogni immagine raster con `_partials/img.html` e ogni acquerello con `_partials/illustrazione.html`, che preferisce il ritaglio PNG.
- **Do** attaccare le didascalie alla foto o al ritaglio che nominano.
- **Do** segnare i fatti mancanti (date, nomi, prezzi, orari) con lo shortcode `da-scrivere`: non si inventano.
- **Do** tenere telefono ed email nel primo schermo (post-it) e in fondo a ogni pagina (chiusura contatti gialla).
- **Do** tenere il focus visibile: contorno inchiostro + anello giallo, contorno giallo sui cartoncini scuri.
- **Do** limitare il movimento alla posa d'ingresso e allo stacco, sempre sotto `prefers-reduced-motion`.

### Don't:
- **Don't** usare gradienti oltre alle due texture del cartellone (zigzag, quaderno a righe).
- **Don't** mettere un'etichetta o un sopratitolo sopra un titolo: le etichette stanno solo accanto ai recapiti.
- **Don't** usare i colori dei bollini (arancio, verde, ciano, rosa, viola) per testo o come fondo di un testo.
- **Don't** scrivere testo sopra una foto senza un fondo pieno di carta.
- **Don't** caricare risorse da domini terzi (font, script, CDN, mappe incorporate) né librerie JS/CSS esterne.
- **Don't** usare ombre nere, colorate o dure senza sfocatura, né angoli morbidi su foto, fogli e card.
- **Don't** introdurre una terza famiglia di caratteri (oltre al corsivo opzionale dei titoli) o il maiuscolo decorativo.
- **Don't** disegnare o generare illustrazioni nuove: si usano solo gli acquerelli del cliente, e se mancano la foto nella stessa cornice.
- **Don't** usare le varianti chiare (`*-chiaro`) come fondo di sezioni nuove: il fondo è sempre un cartoncino pieno.
