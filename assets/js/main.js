// Circo Svago — JS minimo, senza librerie (DESIGN.md §8).

// ---------- Menu mobile ----------
const header = document.querySelector("[data-header]");
const menuToggle = document.querySelector("[data-menu-toggle]");

function chiudiMenu() {
  header?.removeAttribute("data-menu-aperto");
  menuToggle?.setAttribute("aria-expanded", "false");
}

menuToggle?.addEventListener("click", () => {
  const aperto = menuToggle.getAttribute("aria-expanded") === "true";
  menuToggle.setAttribute("aria-expanded", String(!aperto));
  header.toggleAttribute("data-menu-aperto", !aperto);
});

// ---------- Sottomenu ----------
document.querySelectorAll("[data-sottomenu-toggle]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const aperto = btn.getAttribute("aria-expanded") === "true";
    document.querySelectorAll("[data-sottomenu-toggle]").forEach((b) => b.setAttribute("aria-expanded", "false"));
    btn.setAttribute("aria-expanded", String(!aperto));
  });
});

document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  document.querySelectorAll('[data-sottomenu-toggle][aria-expanded="true"]').forEach((b) => b.setAttribute("aria-expanded", "false"));
  if (header?.hasAttribute("data-menu-aperto")) {
    chiudiMenu();
    menuToggle.focus();
  }
});

document.addEventListener("click", (e) => {
  if (!e.target.closest(".nav__voce")) {
    document.querySelectorAll('[data-sottomenu-toggle][aria-expanded="true"]').forEach((b) => b.setAttribute("aria-expanded", "false"));
  }
});

matchMedia("(min-width: 64rem)").addEventListener("change", (e) => { if (e.matches) chiudiMenu(); });

// ---------- Nastro di foto ----------
const nastro = document.querySelector("[data-nastro]");
if (nastro) {
  const passo = () => nastro.clientWidth * 0.8;
  document.querySelector("[data-nastro-prec]")?.addEventListener("click", () => nastro.scrollBy({ left: -passo(), behavior: "smooth" }));
  document.querySelector("[data-nastro-succ]")?.addEventListener("click", () => nastro.scrollBy({ left: passo(), behavior: "smooth" }));
  const prec = document.querySelector("[data-nastro-prec]");
  const succ = document.querySelector("[data-nastro-succ]");
  const aggiorna = () => {
    if (prec) prec.disabled = nastro.scrollLeft <= 2;
    if (succ) succ.disabled = nastro.scrollLeft + nastro.clientWidth >= nastro.scrollWidth - 2;
  };
  nastro.addEventListener("scroll", aggiorna, { passive: true });
  addEventListener("resize", aggiorna);
  aggiorna();
}

// ---------- Lightbox ----------
const lightbox = document.querySelector("[data-lightbox]");
if (lightbox) {
  const img = lightbox.querySelector("[data-lightbox-img]");
  const didascalia = lightbox.querySelector("[data-lightbox-didascalia]");
  let gruppo = [];
  let indice = 0;

  const mostra = (i) => {
    indice = (i + gruppo.length) % gruppo.length;
    const link = gruppo[indice];
    img.src = link.dataset.lightboxSrc;
    img.alt = link.dataset.lightboxAlt || "";
    didascalia.textContent = `${link.dataset.lightboxAlt ? link.dataset.lightboxAlt + " · " : ""}${indice + 1} di ${gruppo.length}`;
  };

  document.addEventListener("click", (e) => {
    const link = e.target.closest("[data-lightbox-src]");
    if (!link) return;
    e.preventDefault();
    gruppo = [...link.closest(".galleria").querySelectorAll("[data-lightbox-src]")];
    mostra(gruppo.indexOf(link));
    lightbox.showModal();
  });

  lightbox.querySelector("[data-lightbox-chiudi]").addEventListener("click", () => lightbox.close());
  lightbox.querySelector("[data-lightbox-prec]").addEventListener("click", () => mostra(indice - 1));
  lightbox.querySelector("[data-lightbox-succ]").addEventListener("click", () => mostra(indice + 1));
  lightbox.addEventListener("click", (e) => { if (e.target === lightbox) lightbox.close(); });
  lightbox.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") mostra(indice - 1);
    if (e.key === "ArrowRight") mostra(indice + 1);
  });
}

// ---------- Styleguide: mostra il valore reale dei token ----------
document.querySelectorAll("[data-token]").forEach((el) => {
  el.textContent = getComputedStyle(document.documentElement).getPropertyValue(el.dataset.token).trim();
});
