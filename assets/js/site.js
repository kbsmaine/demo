const CONFIG = {
  company: 'KBS Commercial Demolition',
  phoneDisplay: '(207) 555-0124',
  phoneHref: 'tel:+12075550124',
  email: 'krpelletier33@gmail.com'
};

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-company]').forEach(el => el.textContent = CONFIG.company);
  document.querySelectorAll('[data-phone]').forEach(el => { el.textContent = CONFIG.phoneDisplay; el.href = CONFIG.phoneHref; });
  document.querySelectorAll('[data-email]').forEach(el => { el.textContent = CONFIG.email; el.href = `mailto:${CONFIG.email}`; });
  document.querySelectorAll('img[data-fallback]').forEach(img => img.addEventListener('error', () => { img.src = img.dataset.fallback; }));

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav-links');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  const filters = document.querySelectorAll('[data-filter]');
  filters.forEach(button => button.addEventListener('click', () => {
    filters.forEach(b => b.classList.remove('active'));
    button.classList.add('active');
    const key = button.dataset.filter;
    document.querySelectorAll('.project').forEach(card => {
      card.classList.toggle('hide', key !== 'all' && card.dataset.category !== key);
    });
  }));
});
