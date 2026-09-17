/* =========================================================
   Entre Luz Home — script.js
   Header scroll, menú mobile, reveal, WhatsApp links, lightbox
   ========================================================= */

(function () {
  'use strict';

  // === CONFIGURACIÓN ===========================================
  // Formato: número internacional sin "+" ni espacios.
  var WSP_NUMERO = '5491166776019';
  var WSP_DEFAULT = 'Hola Entre Luz Home! Quiero pedir un asesoramiento sin cargo para mis cortinas.';
  // =============================================================

  // 1) Links de WhatsApp — cada botón usa su data-wsp-msg o el mensaje por defecto
  document.querySelectorAll('[data-wsp]').forEach(function (el) {
    var msg = el.getAttribute('data-wsp-msg') || WSP_DEFAULT;
    el.setAttribute('href', 'https://wa.me/' + WSP_NUMERO + '?text=' + encodeURIComponent(msg));
    el.setAttribute('target', '_blank');
    el.setAttribute('rel', 'noopener');
  });

  // 2) Estado del header al hacer scroll
  var header = document.querySelector('.site-header');
  var setHeaderState = function () {
    if (window.scrollY > 40) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  };
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });

  // 3) Menú mobile + overlay
  var navToggle = document.querySelector('.nav-toggle');
  var siteNav = document.querySelector('.site-nav');
  if (navToggle && siteNav) {
    var overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    document.body.appendChild(overlay);

    var _scrollY = 0;
    var openNav = function () {
      _scrollY = window.scrollY;
      siteNav.classList.add('is-open');
      overlay.classList.add('is-open');
      header.classList.add('nav-open');
      navToggle.setAttribute('aria-expanded', 'true');
      navToggle.setAttribute('aria-label', 'Cerrar menú');
      document.body.style.overflow = 'hidden';
      document.body.style.position = 'fixed';
      document.body.style.top = '-' + _scrollY + 'px';
      document.body.style.width = '100%';
    };
    var closeNav = function () {
      siteNav.classList.remove('is-open');
      overlay.classList.remove('is-open');
      header.classList.remove('nav-open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.setAttribute('aria-label', 'Abrir menú');
      document.body.style.overflow = '';
      document.body.style.position = '';
      document.body.style.top = '';
      document.body.style.width = '';
      window.scrollTo(0, _scrollY);
      setHeaderState();
    };

    navToggle.addEventListener('click', function () {
      siteNav.classList.contains('is-open') ? closeNav() : openNav();
    });
    overlay.addEventListener('click', closeNav);
    siteNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeNav);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && siteNav.classList.contains('is-open')) closeNav();
    });
  }

  // 4) Reveal al hacer scroll
  var revealEls = document.querySelectorAll(
    '.intro-text, .intro-figure, .product-card, .value-grid li, .gallery-grid figure, .ropacama-grid figure, .process-figure, .process-text, .faq-list, .contact-inner'
  );
  revealEls.forEach(function (el) { el.classList.add('reveal'); });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // 5) Ocultar el botón flotante mientras el hero está a la vista
  var wspFloat = document.querySelector('.wsp-float');
  var heroSection = document.querySelector('.hero');
  if (wspFloat && heroSection && 'IntersectionObserver' in window) {
    var heroObs = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) wspFloat.classList.add('wsp-hidden');
      else wspFloat.classList.remove('wsp-hidden');
    }, { threshold: 0.2 });
    heroObs.observe(heroSection);
  }

  // 6) Año en el footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // 7) Lightbox de galería
  var galleryFigs = document.querySelectorAll('.gallery-grid figure');
  if (galleryFigs.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Vista ampliada de imagen');
    lb.innerHTML =
      '<button class="lb-close" aria-label="Cerrar">&times;</button>' +
      '<button class="lb-prev" aria-label="Anterior">&#10094;</button>' +
      '<img alt="">' +
      '<figcaption></figcaption>' +
      '<button class="lb-next" aria-label="Siguiente">&#10095;</button>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    var items = Array.prototype.map.call(galleryFigs, function (f) {
      var i = f.querySelector('img');
      var webp = f.querySelector('picture source[type="image/webp"]');
      var cap = f.querySelector('figcaption');
      return { src: webp ? webp.getAttribute('srcset') : i.src, alt: i.alt, cap: cap ? cap.textContent : '' };
    });
    var current = 0;
    var lastFocus = null;

    var show = function (i) {
      current = (i + items.length) % items.length;
      lbImg.src = items[current].src;
      lbImg.alt = items[current].alt;
      lbCap.textContent = items[current].cap;
    };
    var open = function (i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb-close').focus();
    };
    var close = function () {
      lb.classList.remove('is-open');
      document.body.style.overflow = '';
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    };

    galleryFigs.forEach(function (f, i) {
      f.setAttribute('tabindex', '0');
      f.setAttribute('role', 'button');
      f.setAttribute('aria-label', 'Ampliar imagen: ' + (f.querySelector('img').alt || ''));
      f.addEventListener('click', function () { open(i); });
      f.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
      });
    });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }
})();
