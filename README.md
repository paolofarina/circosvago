# Circo Svago — sito web

Sorgenti del sito di **Circo Svago**, scuola di circo educativo e sociale ad Albano Laziale.
Il sito è pubblicato su **https://paolofarina.github.io/circosvago/**.

È un sito statico fatto con [Hugo](https://gohugo.io/) (versione extended ≥ 0.146).

## Come si aggiorna

Ogni modifica salvata sul ramo `main` viene pubblicata da sola. GitHub Actions (`.github/workflows/pubblica.yml`)
costruisce il sito e lo mette online in un paio di minuti. Non c'è nessun passaggio a mano.

- **Testi e foto**: ogni pagina è una cartella in `content/`, con un file `index.md` e le sue immagini.
- **Grafica**: le regole di stile sono in `DESIGN.md` e valgono per qualunque modifica a template o CSS.

## Anteprima sul proprio computer

```bash
hugo server
```

Poi apri http://localhost:1313.
