(() => {
  const WORKBENCH = document.querySelector('.monaco-workbench');
  if (!WORKBENCH) return;

  let overlay = null;

  const ensureOverlay = () => {
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'xqk-overlay';
      WORKBENCH.appendChild(overlay);
    }
  };
  const showOverlay = () => { ensureOverlay(); overlay.style.display = 'block'; };
  const hideOverlay = () => { if (overlay) overlay.style.display = 'none'; };

  // Observa aparición/desaparición del Quick Input
  const isVisible = el => el && el.offsetParent !== null;

  const watch = () => {
    const widget = document.querySelector('.monaco-quick-input-widget, .quick-input-widget');
    if (!widget) return;

    // Cada cambio de estilo/clase, decide si mostrar u ocultar overlay
    const update = () => (isVisible(widget) ? showOverlay() : hideOverlay());

    const mo = new MutationObserver(update);
    mo.observe(widget, { attributes: true, attributeFilter: ['style', 'class', 'aria-hidden'] });
    update();

    // Cierra overlay si se destruye el widget
    const rootMo = new MutationObserver(() => {
      if (!document.body.contains(widget)) {
        hideOverlay();
        mo.disconnect();
        rootMo.disconnect();
        setTimeout(watch, 0); // reenganchar para próximos widgets
      }
    });
    rootMo.observe(document.body, { childList: true, subtree: true });
  };

  // Arranque + reintentos por si el DOM tarda
  const tryStart = () => {
    watch();
    // reintenta unas veces por si el widget se crea más tarde
    let tries = 0;
    const t = setInterval(() => { watch(); if (++tries > 20) clearInterval(t); }, 500);
  };

  // Espera a que la UI cargue
  if (document.readyState === 'complete') tryStart();
  else window.addEventListener('load', tryStart);
})();
