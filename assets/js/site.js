/* GUITIN site script: mobile menu, subscribe and sold-out dialogs, shop quantity. No dependencies. */
(function () {
  'use strict';

  /* ---------- mobile menu ---------- */
  var header = document.querySelector('.site-header');
  var menuBtn = document.querySelector('.menu-btn');
  if (header && menuBtn) {
    var setMenu = function (open) {
      header.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? '메뉴 닫기' : '메뉴 열기');
      document.documentElement.style.overflow = open ? 'hidden' : '';
    };
    menuBtn.addEventListener('click', function () { setMenu(!header.classList.contains('is-open')); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    header.querySelectorAll('.nav a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.matchMedia('(min-width: 768px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  /* ---------- dialogs ---------- */
  var dialog = document.getElementById('subscribe');
  function closeDialog() {
    if (!dialog || !dialog.open) return;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) { dialog.close(); return; }
    dialog.classList.add('is-closing');
    setTimeout(function () { dialog.classList.remove('is-closing'); dialog.close(); }, 170);
  }
  function openSubscribe() {
    if (header) { header.classList.remove('is-open'); document.documentElement.style.overflow = ''; }
    dialog.showModal();
  }
  if (dialog && typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-subscribe]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        openSubscribe();
      });
    });
    dialog.querySelector('.modal-close').addEventListener('click', closeDialog);
    dialog.addEventListener('cancel', function (e) { e.preventDefault(); closeDialog(); });
    dialog.addEventListener('click', function (e) { if (e.target === dialog) closeDialog(); });
  }

  /* ---------- sold-out: order is never placed; offer the launch alert instead ---------- */
  var soldout = document.getElementById('soldout');
  if (soldout && dialog && typeof soldout.showModal === 'function') {
    document.querySelectorAll('[data-soldout]').forEach(function (btn) {
      btn.addEventListener('click', function (e) { e.preventDefault(); soldout.showModal(); });
    });
    var closeSoldout = function () { soldout.close(); };
    soldout.querySelector('.modal-close').addEventListener('click', closeSoldout);
    soldout.querySelector('[data-dismiss]').addEventListener('click', closeSoldout);
    soldout.addEventListener('click', function (e) { if (e.target === soldout) closeSoldout(); });
    soldout.querySelector('[data-go-subscribe]').addEventListener('click', function () {
      soldout.close();
      openSubscribe();
    });
  }

  /* ---------- quantity stepper (shop) ---------- */
  var qty = document.getElementById('qty');
  if (qty) {
    var minus = document.querySelector('[data-qty="-1"]');
    var setQty = function (n) { n = Math.max(1, Math.min(10, n)); qty.textContent = n; minus.disabled = n <= 1; };
    document.querySelectorAll('[data-qty]').forEach(function (b) {
      b.addEventListener('click', function () { setQty(Number(qty.textContent) + Number(b.getAttribute('data-qty'))); });
    });
    setQty(1);
  }

})();
