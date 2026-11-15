---
target: home + acrobatica aerea + circus playground
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:C:\\Progetti\\circosvago-impeccable\\layouts\\home.html"
target_fingerprint: "sha256:ca5b1ea2087b3b831ffabb1648933e0ce0bfed32d66b61bd23766bea5a8cd656"
target_path: "C:\\Progetti\\circosvago-impeccable\\layouts\\home.html"
timestamp: 2026-11-13T20-21-33Z
slug: layouts-home-html
---
Method: dual-agent (A: design review sub-agent · B: detector/browser sub-agent)

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Nastro prev/next never disable at the ends |
| 2 | Match System / Real World | 3 | Generic h1 "Benvenuti a Circo Svago"; "Altro in Eventi e feste" reads templated |
| 3 | User Control and Freedom | 3 | Mobile menu closes only via its own button |
| 4 | Consistency and Standards | 2 | Photo inside the watercolour series; focus treatment differs per component |
| 5 | Error Prevention | 3 | Post-it email breaks mid-domain on desktop; CTAs hop to /contatti/ |
| 6 | Recognition Rather Than Recall | 3 | 29 tab stops through open-on-focus submenus before the hero CTA |
| 7 | Flexibility and Efficiency | n/a | Brochure surface, no repeat expert users (tel:/mailto: present) |
| 8 | Aesthetic and Minimalist Design | 3 | Home ~10,100px at 390, overlapping sections |
| 9 | Error Recovery | 3 | Small surface, no inputs |
| 10 | Help and Documentation | n/a | FAQ facts deliberately missing ("Da scrivere") |
| **Total** | | **23/32** | **Good (72%)** |

## Design Specificity Verdict

LLM: authored for Circo Svago — card-stock fields from the brochure, client watercolours as taped cut-outs, marker headings, contact post-it in every first viewport, a real material vocabulary in carta.css. Soft spot: tape + white-bordered prints is a scrapbook trope that turns generic where the client art is missing (Circus Playground hero, event cards, "Corpo e movimento").
Deterministic: bundled detector and npx impeccable 4.9.0 agree — home 0, acrobatica 1 (nested-cards on aside.da-scrivere: false positive, placeholder post-it), circus playground 0. Template/CSS scans partial (unresolved Hugo stylesheet link). Overlay skipped by instruction.
Measured: 0 contrast failures, 0 missing alt, 1 h1 per page, no horizontal overflow at 375/390/1440, no third-party requests, reduced motion disables the entrance. Fonts: Nunito and Yellowtail are still preloaded (leftover). Focus invisible on dark card stock.

## Priority Issues

- [P1] Keyboard focus invisible on prints/arrows/scroller on the black cartoncino; yellow focus ring stripped from .btn and .staccabile (specificity). Fix: yellow ring on :focus-visible for .btn/.staccabile, yellow outline inside dark cartoncini. → harden
- [P1] Hero post-it email wraps mid-domain at desktop. Fix: --t-base, <wbr> before @, wider post-it. → polish
- [P1] Home repeats the same choice four times (nastro 11 links, Cosa facciamo, corsi, eventi), duplicated Scuola sentence, the selling line "Aspetta… ma questa cosa la so fare davvero?" buried. Fix: nastro as proof not navigation, drop duplicate lead, bring the bubble into the hero. → distill, clarify
- [P2] Cut-out series breaks where art is missing (Corpo e movimento as photo print). Fix: same ritaglio frame for photo fallback; never invent art. → polish
- [P2] In-page CTAs leave the designed flow to /contatti/. Fix: jump to the page's own contact close. → clarify
- [P3] Mobile menu has no contact inside. → adapt

## Persona Red Flags

Jordan: generic h1; "Da scrivere" looks like the contact post-it. Riley: email break, invisible focus, nastro arrows never disable, 29 tab stops. Casey: phone above the fold everywhere (good), home ~12 screens. Parent from Instagram: phone immediate; ages/times missing (marked). Event organiser: strong photo proof; logistics facts missing (should be marked, not invented).

## Minor Observations

Shantell at 15px for labels/captions; Atkinson slashed zeros in dates/postcode; malva h2 is a two-sentence display heading; header logo small; lightbox caption crowded; ragged last gallery row; leftover Nunito/Yellowtail preloads (~58KB).

## Questions to Consider

If the selling moment is "Aspetta… ma questa cosa la so fare davvero?", why is the biggest text "Benvenuti"? Should "Momenti di circo" be proof instead of 11 more doors? What is the hand-made signature where watercolours are absent?
