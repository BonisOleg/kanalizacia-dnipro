(function () {
  'use strict';

  // =====================
  // MOBILE MENU TOGGLE
  // =====================
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      const isOpen = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', String(!isOpen));
      mobileMenu.setAttribute('aria-hidden', String(isOpen));
      mobileMenu.classList.toggle('mobile-menu--open', !isOpen);
      document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    // Close menu on outside click
    document.addEventListener('click', function (e) {
      if (
        mobileMenu.classList.contains('mobile-menu--open') &&
        !mobileMenu.contains(e.target) &&
        !hamburger.contains(e.target)
      ) {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        mobileMenu.classList.remove('mobile-menu--open');
        document.body.style.overflow = '';
      }
    });

    // Close menu on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobileMenu.classList.contains('mobile-menu--open')) {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        mobileMenu.classList.remove('mobile-menu--open');
        document.body.style.overflow = '';
        hamburger.focus();
      }
    });

    // Close menu when navigating (mobile links)
    mobileMenu.querySelectorAll('.mobile-nav__link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        mobileMenu.classList.remove('mobile-menu--open');
        document.body.style.overflow = '';
      });
    });
  }

  // =====================
  // HEADER SCROLL SHADOW
  // =====================
  const header = document.querySelector('.site-header');
  if (header) {
    const observer = new IntersectionObserver(
      function ([entry]) {
        header.classList.toggle('site-header--scrolled', !entry.isIntersecting);
      },
      { threshold: 0, rootMargin: '-' + getComputedStyle(document.documentElement).getPropertyValue('--header-height') + ' 0px 0px 0px' }
    );
    // Observe a sentinel element placed right after the header space
    const sentinel = document.createElement('div');
    sentinel.style.cssText = 'position:absolute;top:1px;left:0;width:1px;height:1px;pointer-events:none;';
    document.body.prepend(sentinel);
    observer.observe(sentinel);
  }

  // =====================
  // FAQ ACCORDION
  // =====================
  document.querySelectorAll('.faq__question').forEach(function (dt) {
    dt.addEventListener('click', toggleFaq);
    dt.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleFaq.call(this);
      }
    });
  });

  function toggleFaq() {
    const expanded = this.getAttribute('aria-expanded') === 'true';
    // Close all others
    document.querySelectorAll('.faq__question[aria-expanded="true"]').forEach(function (el) {
      if (el !== this) {
        el.setAttribute('aria-expanded', 'false');
        const dd = el.nextElementSibling;
        if (dd) dd.hidden = true;
      }
    }, this);
    this.setAttribute('aria-expanded', String(!expanded));
    const answer = this.nextElementSibling;
    if (answer) answer.hidden = expanded;
  }

  // =====================
  // QUIZ — radio auto-advance
  // =====================
  document.body.addEventListener('htmx:afterSettle', function () {
    attachQuizRadios();
    attachFaqHandlers();
  });

  function attachQuizRadios() {
    document.querySelectorAll('.quiz__radio').forEach(function (radio) {
      if (radio.dataset.autoAdvanceAttached) return;
      radio.dataset.autoAdvanceAttached = '1';
      radio.addEventListener('change', function () {
        // Wait a tick so user sees selection, then submit
        const form = this.closest('.quiz__form');
        if (form) {
          setTimeout(function () {
            if (form.querySelector('[type="tel"]')) return; // step 4 — don't auto-submit
            form.requestSubmit();
          }, 350);
        }
      });
    });
  }
  attachQuizRadios();

  function attachFaqHandlers() {
    document.querySelectorAll('.faq__question').forEach(function (dt) {
      if (dt.dataset.faqAttached) return;
      dt.dataset.faqAttached = '1';
      dt.addEventListener('click', toggleFaq);
      dt.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggleFaq.call(this);
        }
      });
    });
  }

  // =====================
  // SMOOTH SCROLL (for browsers that don't support CSS scroll-behavior)
  // =====================
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const top = target.getBoundingClientRect().top + window.scrollY - parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height'), 10) - 16;
        window.scrollTo({ top: top, behavior: 'smooth' });
        target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
      }
    });
  });

})();
