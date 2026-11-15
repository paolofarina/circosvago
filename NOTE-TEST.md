# Note del test — skill Impeccable

Copia di test `C:\Progetti\circosvago-impeccable`, branch `test/impeccable`. Skill: **Impeccable 0.1.23** (`.claude/skills/impeccable`), unica skill di design installata. Modalità del brief: "carta bianca".
Anteprima: `hugo server --port 1314`. Screenshot in `test-screenshot/` (1440 e 390 px, pagina intera, catturati con Playwright e `prefers-reduced-motion` per avere l'animazione d'ingresso già posata).

## Risultato in una riga

Mondo visivo nuovo, **"il cartellone di classe"**: ogni sezione è un cartoncino colorato a tutta pagina con il bordo tagliato a zigzag. Sopra ci sono fogli bianchi per il testo, gli acquerelli del cliente ritagliati con le forbici, le foto stampate col bordo bianco e il nastro di carta, un post-it giallo con i contatti, i titoli "a pennarello".

---

## 1. Comandi e strumenti della skill, in ordine

| # | Passo | Cosa ha fatto |
|---|---|---|
| 1 | `impeccable context` | Ha letto `DESIGN.md`, nessun `PRODUCT.md` → ha chiesto l'`init`. Non ha riconosciuto i template Hugo come "implementazione visiva" (`hasVisualImplementation: false`). |
| 2 | `/impeccable init` | Ha scritto `PRODUCT.md`. Le risposte all'intervista sono prese dal brief, come chiesto dalla sessione madre; non ho fatto domande all'utente. |
| 3 | `concept-seed --scope direction --mode persuade` | Ha tirato i dadi tra 7 direzioni che ho ricavato dal mondo del pubblico (brochure, quaderno d'acquerelli, gioco dell'oca, **cartellone di classe**, affissioni, biglietti della sagra, tendone). È uscita la n. 4. Ha anche proposto 6 "sfidanti" dal catalogo (copertina jazz, figurine, carta marmorizzata, display di particelle, tensegrità, immersione): li ho scartati tutti. Da tre ho preso una disciplina ciascuno: un colore pieno per sezione, una serie coerente, didascalie attaccate. Il catalogo è stato scaricato da impeccable.style (`source: api`) anche con la telemetria spenta. |
| 4 | `serve-question` (pagina di scelta) | Pagina locale con le carte delle direzioni, aperta nel browser dell'app. Nessuna risposta in ~5 minuti → ho costruito la direzione assegnata. **Non** ho mandato il ping di telemetria della scelta (`--kind`), per rispetto di `telemetry: false`. |
| 5 | `surface-brief write` | Contratto di direzione in `.impeccable/surfaces/layouts-home-html.md` (tesi, mondo, storia, prima schermata, forma, seed). |
| 6 | `craft-floor.md` + costruzione | Build "code-led": la skill non aveva generazione di immagini, quindi niente comp da imitare. |
| 7 | Hook PostToolUse | **Funziona su Windows** (Git Bash): ha controllato ogni Edit/Write. Non ha mai segnalato nulla sui sorgenti; dopo 6 modifiche allo stesso file smette di dare indicazioni. |
| 8 | `/impeccable critique` | Due sotto-agenti isolati: A (revisione di design) e B (rilevatore + misure Playwright). Punteggio **23/32** (euristiche 7 e 10 n/a), 3 problemi P1. Salvato in `.impeccable/critique/`. Le domande finali all'utente le ho saltate (prova non presidiata). |
| 9 | `/impeccable polish` | Ho corretto i P1 e parte dei P2 della critique (vedi §3). |
| 10 | `impeccable detect` + `npx impeccable detect` (4.9.0) | Sulle 3 URL a 1440 e 390: home **0**, circus-playground **0**, acrobatica-aerea **1** (`nested-cards` sul post-it "Da scrivere": falso positivo; l'eccezione è registrata solo per quel partial e vale per l'hook, la scansione per URL continua a mostrarlo — rilancio finale: stesso risultato). Sui soli file sorgente il detector è cieco: non risolve il link CSS di Hugo e lo dice. |
| 11 | `/impeccable audit` | **16/20**. Salvato in `.impeccable/audit/`. |
| 12 | `impeccable-finish-reviewer` (sotto-agente) | Primo verdetto `fix` con 8 correzioni. Le ho applicate tutte, poi ho mandato le nuove catture allo stesso revisore: 5 risolte, 1 parziale, 2 da finire, più 2 regressioni nuove. Ho chiuso anche quelle (§3, giro 3). Non c'è stato un terzo verdetto: la skill fissa a due giri il budget di una prova non presidiata. |
| 13 | `impeccable-documenter` (sotto-agente) | Ha riscritto `DESIGN.md` dal codice costruito e creato `.impeccable/design.json` (scelta "overwrite", presa da me). |
| 14 | Hook Stop | Analizza anche `public/` (l'output della build) e segnala `cramped-padding` sulle sezioni a tutta larghezza e "strisce decorative" sulle righe del quaderno. Sono falsi positivi: è un'analisi statica che non vede il margine interno del `.contenitore`, e le scansioni sulle URL renderizzate sono pulite. Li ho lasciati stare: non sono soppressi. |

Non usati, come da istruzioni: `/impeccable live` e lo `live-server` con l'overlay.

## 2. Scelte di design e perché

- **Mondo: il cartellone di classe.** È il manufatto che famiglie, scuole ed enti conoscono a memoria dai laboratori. Porta il "fatto a mano" del brief senza cadere nel solito circo vintage (strisce rosse e bianche, lettering Barnum). Accoglie anche le illustrazioni del cliente come ritagli, che restano le protagoniste.
- **Palette: cartoncini pieni.** Strategia "full palette", un colore per sezione, nessun fondo crema.
  - I colori (tutti in `tokens.css`, con i contrasti misurati in commento):
    - giallo `#F5C518`, inchiostro sopra 10.4:1;
    - rosso `#C2452F`, bianco sopra 5.0:1;
    - malva `#8C3B7C`, 6.9:1;
    - blu `#2C5AA8`, 6.7:1;
    - nero album `#1E1A2B`;
    - bianco.
  - Rosso, malva e blu sono quelli della brochure, solo un po' più profondi. Il giallo viene dal logo.
  - Bollini adesivi (arancio, verde, ciano, rosa, viola dal logo) solo per decorare.
- **Font self-hosted (OFL, scaricati in `static/fonts/`).**
  - **Shantell Sans** per i titoli, perché sembra pennarello ma resta leggibile.
  - **Atkinson Hyperlegible Next** per il testo: pubblico ampio, scuole ed enti.
  - Peso dei font sceso da 171 a 114 KB: tolti Nunito, Yellowtail e Josefin.
- **Layout.**
  - **Home:** apertura gialla con titolo enorme, striscia con il lead, due bottoni-etichetta, post-it con telefono ed email della segreteria, e la balena ritagliata storta col nastro. Seguono:
    - "Momenti di circo": foto stampate sul cartoncino nero dell'album, ora come prova e non come link;
    - "Chi siamo" su un foglio di quaderno;
    - "Cosa facciamo", con la Scuola come pezzo grande;
    - la serie dei corsi ritagliati;
    - gli eventi, che a 390 px scorrono di lato;
    - la chiusura gialla con i contatti.
  - **Pagine corso ed evento:** testata del colore di sezione con la foto stampata e il ritaglio, post-it con il contatto giusto (segreteria@ per i corsi, eventi@ per gli eventi). Poi:
    - il testo su un foglio;
    - la galleria a collage con lightbox;
    - "gli altri corsi" come ritagli, o "altro in Eventi" come foto;
    - la chiusura contatti.
  - I bottoni nel testo ("Chiedi informazioni", "Porta il Playground al tuo evento") ora saltano alla chiusura contatti della pagina stessa.
- **Interazione firma.** I pezzi "si staccano" al passaggio o al focus (si alzano e si raddrizzano). All'apertura i pezzi della testata si posano uno alla volta, solo se `prefers-reduced-motion: no-preference`.
- **Ritagli veri.** `tools/ritaglia_illustrazioni.py` toglie il fondo carta dalle scansioni del cliente e aggiunge un margine bianco irregolare "da forbici". Il risultato sono i PNG con trasparenza in `assets/img/illustrazioni/ritagli/`, con la provenienza incorporata. Nessun disegno è stato inventato.

## 3. Cosa la skill ha fatto bene, cosa ha sbagliato, cosa ho corretto a mano

**Bene**
- Il processo obbliga a decidere una direzione con un punto di vista. Il tiro dei dadi mi ha tolto dalla scelta più ovvia (la brochure rifatta, cioè il sito attuale), che la skill stessa indicava come "rut". Il risultato è riconoscibile ma non è il sito di prima.
- `craft-floor.md` è utile e concreto: niente etichette sopra i titoli, focus, contrasto, selezione del testo, refusi dei default del browser.
- La **critique a due agenti isolati** ha trovato problemi reali che avevo mancato:
  - focus invisibile sul cartoncino nero, perché la specificità di `.staccabile:focus-within` copriva l'anello giallo;
  - l'email nel post-it spezzata a metà dominio;
  - la frase "Il gioco e il divertimento…" ripetuta due volte;
  - due font vecchi ancora precaricati.
- Il **revisore finale** è stato severo e utile: ritagli che erano solo rettangoli bianchi, "Cosa facciamo" ancora a card uguali, tessera "Centri estivi" vuota a 390 px, `DESIGN.md` obsoleto.
- Il rilevatore gira davvero sulle URL, ed è identico in versione bundled e npm.
- L'hook funziona su Windows.

**Male, o ignorato**
- **Pesante e lento.** Il processo vuole tante cose:
  - domande all'utente (init, scelta della direzione, critique, documenter);
  - pagine locali da cui aspettare una risposta;
  - 5 sotto-agenti;
  - file di stato.

  In una prova senza nessuno a rispondere, ho dovuto decidere io e annotarlo a ogni passo.
- `context` non ha riconosciuto il progetto Hugo esistente come implementazione visiva.
- Il catalogo dei "challenger" è stato scaricato dalla rete anche con la telemetria spenta. Il ping della scelta lo avrebbe mandato se non lo avessi saltato.
- Le direzioni pescate dal catalogo erano quasi tutte fuori tema per una scuola di circo per famiglie (acceleratore di particelle, immersione profonda, tensegrità).
- Il detector sui file sorgente non vede nulla, perché non risolve il CSS di Hugo. L'hook Stop invece analizza `public/` e produce falsi positivi su ogni pagina con sezioni a tutta larghezza.
- La critique (agente A) e il revisore finale si sono contraddetti sul fumetto "Aspetta… ma questa cosa la so fare davvero?". La prima lo voleva nell'apertura, il secondo lo ha giudicato un duplicato. Ho seguito il revisore.
- La skill non aiuta a ricavare asset come i ritagli senza generazione di immagini: lo script l'ho scritto io.

**Correzioni a mano (oltre a quelle chieste dalla skill)**
- Errore mio: virgolette dentro il front matter della styleguide hanno rotto la build per qualche minuto. Me ne sono accorto dal log del server e l'ho corretto prima degli screenshot finali.
- Errore mio: `aspect-ratio: auto` annullava il rapporto dell'immagine. La sagoma di "Centri estivi" risultava larga 0 px e non si caricava; trovato con Playwright.
- Frecce del nastro che non si disattivavano agli estremi, e che a pagina appena caricata partivano già scrollate di 96 px (snap padding).
- Contatti nel menu mobile, target di tocco portati a 44 px, sottomenu desktop che non si aprono più a ogni Tab: da 29 a 12 tab prima del primo bottone.
- `tools/controlla_design.py` aggiornato: ammette solo le texture di `carta.css` come gradienti. Pagina `/styleguide/` aggiornata con i cartoncini e i materiali. Partial `onda.html` rimosso.

**Correzioni del revisore finale, giro 3 (dopo il secondo verdetto)**
- Balena di nuovo storta (-3.5°) e fissata col nastro.
- Eventi e Progetti compatti anche su telefono.
- Niente banda vuota sotto la striscia eventi.
- Prova a 390 px della tessera "Centri estivi" in `.impeccable/review/mobile-eventi-fine.png`.

Nessun verdetto dopo questo giro: le correzioni sono verificate solo da me, con screenshot e misure Playwright.

## 4. Misure finali (Playwright, server di sviluppo)

- **Contrasto:** 0 coppie sotto AA su ~400 testi controllati (1440, 390, 375).
- **Scroll orizzontale:** nessuno a 375, 390 e 1440.
- **Risorse esterne:** 0 richieste a host diversi da localhost; nessun errore in console.
- **Struttura e alt:** 1 `h1` per pagina, nessun salto di livello; `alt` su tutte le immagini di contenuto.
- **Movimento ridotto:** `prefers-reduced-motion` toglie l'animazione d'ingresso.
- **Peso al primo caricamento a 390 px**, senza contare `livereload.js` (80 KB, solo in sviluppo):
  - home ≈ 380 KB;
  - corso ≈ 255 KB;
  - evento ≈ 280 KB.

## 5. Tempo e iterazioni

- **Tempo:** circa 1 ora e 10 minuti di lavoro (20:52 → ~22:00). Contiene ~5 minuti di attesa sulla pagina di scelta e ~15 minuti di sotto-agenti.
- **Iterazioni:** 4 giri visivi sulle tre pagine:
  1. prima costruzione;
  2. correzioni viste da me;
  3. polish dalla critique;
  4. correzioni del revisore finale (2 verdetti), più un giro finale senza verdetto.
- **Sotto-agenti:** 5 (critique A, critique B, revisore finale ×2 passaggi, documentatore).

## 6. File prodotti dalla skill

- `PRODUCT.md` — verità di prodotto, dall'init.
- `DESIGN.md` — riscritto dal documentatore sul sistema costruito.
- `.impeccable/` — config (telemetria spenta, un'eccezione del detector), contratto di direzione, report di critique e audit, `design.json`, catture del revisore.

  La cartella è ignorata dal `.gitignore` della copia di test: nel commit ho aggiunto solo i file utili al confronto.

---

## 7. Secondo giro, su richiesta dell'utente (15 novembre)

Richiesta: sito più sobrio, colori un po' meno forti, nuova immagine per Corpo e movimento, proposte di font prima di rifare tutto, poi una prova col corsivo dei titoli della brochure e il riuso dei disegni della brochure.

- **Font.** Quattro coppie confrontate sulla stessa testata (`test-screenshot/proposte-font.png`: Shantell più leggero, Bricolage Grotesque, Fredoka, Kalam + Figtree). L'utente ha tenuto **Shantell Sans**, ora a peso 700/650 invece di 800.
- **Corsivo della brochure.**
  - Nel PDF i titoli sono tracciati vettoriali (i soli font incorporati sono Avenir Black e Book), quindi il nome non si legge.
  - Il `font-match` di Impeccable fallisce sui corsivi legati: ha visto 3 "glifi" e ha proposto font a mano libera non pertinenti.
  - Il confronto a occhio con 16 corsivi gratuiti e una ricerca web dicono che è un corsivo monolineare commerciale, simile ad Akin o Monoline Script, non identificato con certezza.
  - Il gratuito più vicino è **Style Script**. È attivabile con `titoli = "corsivo"` in `hugo.toml` (default `"pennarello"`); confronto in `test-screenshot/prova-titoli-corsivo.png`.
- **Colori.** Cartoncini circa il 25% meno saturi: giallo `#F1D06B`, rosso `#AD5344`, malva `#814675`, blu `#3D5E97`, scuro `#2B2735`; post-it e bollini più tenui. Tutti i contrasti restano AA, misurati: 0 coppie sotto soglia.
- **Sobrietà.**
  - Inclinazioni dimezzate con un solo token (`--k-storto: .5`).
  - Ombre più corte, zigzag più fine.
  - Titoli più piccoli (massimo 5rem).
  - Nastro adesivo tolto dalle foto in serie (nastro, card, blocchi).
- **Corpo e movimento.** L'immagine dell'utente è stata ritagliata come gli altri acquerelli: l'etichetta già stampata è stata tolta, e c'è una soglia dedicata nello script per non tenere l'ombra grigia. Ora compare nella serie dei corsi e nella testata della pagina.
- **Elementi della brochure.** Estratti come SVG vettoriali da `tools/estrai_elementi_brochure.py`, inseriti con `_partials/elemento.html`, al massimo uno per sezione:
  - birilli nel footer;
  - monociclo nella chiusura contatti;
  - giocoliere nella testata di Circus Playground, che non aveva un disegno;
  - biciclo e clave a linee accanto ai titoli dei corsi e degli eventi in home.
- **Peso.** Gli SVG aggiungono circa 110 KB non compressi alla home (75 KB solo il biciclo). Con gzip in produzione diventano circa un quarto.
- **Rilevatore.** Invariato: home 0, playground 0, acrobatica 1 (il post-it "Da scrivere").
