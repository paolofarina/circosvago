# Product

<!-- impeccable:product-schema 1 -->

> Scritto durante `/impeccable init` nella copia di test. Le risposte all'intervista sono state prese da `BRIEF-TEST.md`
> (istruzione esplicita della sessione che ha avviato la prova: "rispondi usando il brief"). Ogni riga deriva dal brief,
> da `hugo.toml`, dai testi in `content/` o dalla brochure 2025; nulla è stato inventato.

## Platform

web

## Users

- **Famiglie con bambini** che cercano un corso o un'attività per i figli: arrivano da telefono, spesso da Instagram o da un volantino.
- **Ragazzi e adulti** che vogliono provare una disciplina (acrobatica aerea, giocoleria, equilibrismo, swing, hip hop, acroyoga…).
- **Organizzatori di feste ed eventi** (compleanni, fiere, festival, piazze) che vogliono portare il circo da loro.
- **Scuole ed enti pubblici** interessati a laboratori, circo educativo e circo sociale.

Il lavoro del visitatore: capire in pochi secondi che cosa si può fare qui, sentirsi invitato, e scrivere o telefonare.

## Product Purpose

Circo Svago è una scuola di circo educativo e sociale ad Albano Laziale (Castelli Romani, Roma), attiva dal 2015.
È tre cose insieme: una scuola di corsi, una compagnia che fa spettacoli ed eventi, un'associazione che porta il circo
nelle scuole e nei progetti sociali.

Il sito ha successo quando fa venire voglia di **provare un corso** e quando fa **richiedere un evento o un laboratorio**.

## Positioning

Non uno spettacolo da guardare: un posto dove si entra, si prova e si cresce insieme. "Aspetta… ma questa cosa la so fare
davvero?" è il momento che la scuola vende. Il circo come gioco, fiducia e comunità, fatto a mano (anche i giochi in legno
del Circus Playground sono costruiti a mano).

## Operating Context

- Il visitatore tipo arriva da telefono, da un post Instagram o da un volantino/brochure cartacea.
- La brochure 2025 è il riferimento cartaceo che il pubblico ha già in mano: pagine a campitura piena (corallo, malva, blu),
  titoli in corsivo-script, illustrazioni ad acquerello, logo multicolore.
- Contatti reali (da `hugo.toml`): Piazza A. Moro 45, 00041 Albano Laziale (RM) · +39 331 868 1147 (Jacopo) ·
  info@ · segreteria@ · eventi@circosvago.it. Profili social non ancora forniti.
- Non esiste ancora un modulo di contatto attivo: si contatta via email e telefono.

## Capabilities and Constraints

- Sito statico **Hugo** (extended ≥ 0.146). Niente framework JS, niente build Node per il sito.
- **Nessuna risorsa da domini terzi** (GDPR): font, script, mappe tutto self-hosted.
- Contenuti nei file `content/**/index.md` (page bundle con foto ottimizzate e testi alternativi nel front matter).
- Dati non ancora forniti dal cliente e da **non inventare**: orari, età, prezzi, insegnanti, date degli eventi,
  link social. Si segnano con lo shortcode `da-scrivere`.
- Terminologia fissa: **Circo Svago**, **Circus Playground**, **Città Circenz(s)e**, **LabBOLLA**, **Re-Play**.

## Brand Commitments

- **Logo** multicolore con motto *"Be a rebel. Join the circus."* (`assets/img/logo/`, versione nera e bianca).
- **Illustrazioni ad acquerello** del cliente (balena con tendone, trapezio, cerchio, giocoliere, swing, hip hop) in
  `assets/img/illustrazioni/`: sono l'elemento più riconoscibile del marchio e vanno usate come protagoniste.
- **Tono**: caldo, giocoso, inclusivo, fatto a mano. Mai corporate, mai "charity" generico. Si dà del tu, frasi brevi.

## Evidence on Hand

- Foto vere di allievi, spettacoli e giochi in legno nei page bundle (42 foto, alt nel front matter).
- Testi del cliente in `content/` (home, sezioni, pagine corso ed evento).
- Brochure 2025 (sola lettura, fuori dal progetto).
- **Assenti**: testimonianze, numeri di allievi, premi, recensioni, prezzi, calendario. Non vanno fabbricati.

## Product Principles

1. **Invitare a provare, non a guardare.** Ogni pagina finisce con un modo concreto di contattare.
2. **Le illustrazioni e le persone vere prima di tutto.** Acquerelli e foto reali portano l'identità; il resto le serve.
3. **Telefono prima.** Chi arriva da Instagram deve capire e agire con un pollice.
4. **Mai inventare.** Ciò che manca si dichiara come mancante.

## Accessibility & Inclusion

Pubblico ampio (bambini, genitori, scuole, enti pubblici): contrasto WCAG AA (testo ≥ 4.5:1, grande ≥ 3:1), focus visibile,
`prefers-reduced-motion` rispettato, `alt` su tutte le immagini, nessuno scroll orizzontale a 375px.
