# Brief del test: tre skill di design a confronto

Questo brief è **identico** per tutte e tre le prove (Impeccable, Taste Skill, UI/UX Pro Max).
Ogni prova lavora nella propria copia del progetto (git worktree, branch `test/<skill>`) e usa **una sola skill**.

## Il cliente

**Circo Svago** — scuola di circo educativo e sociale ad Albano Laziale (Castelli Romani, Roma), dal 2015.
È una scuola di corsi (acrobatica aerea, giocoleria, equilibrismo, swing, hip hop, acroyoga…), una compagnia che fa spettacoli ed eventi,
e un'associazione che porta il circo nelle scuole e nei progetti sociali.

- **Pubblico**: famiglie con bambini, ragazzi, adulti che vogliono provare; organizzatori di feste ed eventi; scuole ed enti pubblici.
- **Obiettivo del sito**: far venire voglia di provare un corso e far richiedere eventi/laboratori.
- **Tono**: caldo, giocoso, inclusivo, fatto a mano. Mai corporate. Motto del logo: *"Be a rebel. Join the circus."*
- **Il visitatore tipo** arriva da telefono, spesso da Instagram o da un volantino.

## Materiale disponibile

- Testi: già nei file `content/**/index.md` e `_index.md` (presi dal cliente, **non inventare** fatti, date, orari, prezzi, nomi).
- Foto vere, già ottimizzate, nelle cartelle delle pagine (`content/.../*.jpg`), con testo alternativo nel front matter.
- Illustrazioni ad acquerello del cliente in `assets/img/illustrazioni/` (balena con tendone, trapezio, cerchio, giocoliere, swing, hip hop): sono l'elemento più riconoscibile del marchio.
- Logo in `assets/img/logo/` (versione scritta nera e scritta bianca).
- Brochure 2025 e materiale grezzo (sola lettura, **non copiare** nel progetto): `C:\Progetti\circosvago\CIRCO SVAGO SITO\`.
- Il sito attuale (versione di riferimento) gira su http://localhost:1313 dal progetto originale.

## Cosa produrre

Ridisegnare **solo queste tre pagine**, come proposta della skill:

1. **Home** — `content/_index.md`, template `layouts/home.html`
2. **Acrobatica aerea** — `content/scuola/acrobatica-aerea/` (pagina corso, molte foto + illustrazione)
3. **Circus Playground** — `content/eventi/circus-playground/` (pagina evento, galleria, invito a contattarci)

Le altre pagine possono cambiare aspetto di conseguenza (header, footer, CSS condiviso): non vengono valutate, ma il sito deve continuare a funzionare.

## Regole del test

**Libertà (modalità "carta bianca")**: la skill può proporre palette, font, layout e componenti diversi da quelli attuali.
`DESIGN.md` e `assets/css/tokens.css` descrivono la versione attuale: usali come riferimento, non come vincolo.

**Vincoli non negoziabili** (valgono per tutte e tre le prove):
- Resta un sito **Hugo** (`hugo` deve compilare senza errori). Niente framework JS, niente build Node per il sito.
- **Contenuti veri**: niente testi segnaposto, niente foto stock o d'archivio spacciate per foto del cliente.
- **Nessuna risorsa da domini terzi** caricata dalla pagina (font, script, CDN): tutto self-hosted (GDPR). I font possono cambiare, ma vanno scaricati in `static/fonts/`.
- **Accessibilità**: contrasto testo ≥ 4.5:1 (≥ 3:1 per testo grande), focus visibile, `prefers-reduced-motion` rispettato, immagini con `alt`.
- **Mobile first**: deve funzionare a 375px senza scroll orizzontale.
- Non toccare `C:\Progetti\circosvago` (il progetto originale) né le altre copie di test.

## Consegna

Alla fine della prova, nella radice della copia:

1. `NOTE-TEST.md` con:
   - comandi/strumenti della skill usati e in che ordine;
   - scelte di design (palette, font, layout) e perché;
   - cosa la skill ha fatto bene, cosa ha sbagliato o ignorato, cosa hai dovuto correggere a mano;
   - tempo indicativo e numero di iterazioni.
2. Screenshot delle tre pagine a **1440px** e **390px** in `test-screenshot/` (`home-1440.png`, `home-390.png`, `aerea-1440.png`, …).
3. Un commit sul branch `test/<skill>` con tutto il lavoro.

## Criteri di valutazione (per il confronto finale)

| Criterio | Peso |
|---|---|
| Identità: sembra Circo Svago (illustrazioni, brochure, logo)? | 25% |
| Chiarezza: si capisce subito cosa offre e come contattare? | 20% |
| Resa su telefono | 15% |
| Accessibilità misurata (contrasto, focus, struttura) | 15% |
| Peso e velocità della pagina | 10% |
| Manutenibilità in Hugo (contenuti nei .md, template puliti) | 15% |
