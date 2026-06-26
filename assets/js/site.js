const CONFIG = {
  company: 'KBS Demolition',
  phoneDisplay: '(207) 590-3771',
  phoneHref: 'tel:+12075903771',
  email: 'service@kbsdemolition.com'
};

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-company]').forEach((element) => {
    element.textContent = CONFIG.company;
  });

  document.querySelectorAll('[data-phone]').forEach((element) => {
    element.textContent = CONFIG.phoneDisplay;
    element.href = CONFIG.phoneHref;
  });

  document.querySelectorAll('[data-email]').forEach((element) => {
    element.textContent = CONFIG.email;
    element.href = `mailto:${CONFIG.email}`;
  });

  document.querySelectorAll('img[data-fallback]').forEach((image) => {
    image.addEventListener('error', () => {
      image.src = image.dataset.fallback;
    });
  });

  // Keep successful quote submissions on this website instead of FormSubmit's default page.
  document.querySelectorAll('[data-formsubmit-next]').forEach((field) => {
    const current = new URL(window.location.href);
    const basePath = current.pathname.replace(/[^/]*$/, '');
    field.value = `${current.origin}${basePath}thank-you.html`;
  });

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav-links');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  const filters = document.querySelectorAll('[data-filter]');

  filters.forEach((button) => {
    button.addEventListener('click', () => {
      filters.forEach((filterButton) => {
        filterButton.classList.remove('active');
      });

      button.classList.add('active');
      const key = button.dataset.filter;

      document.querySelectorAll('.project').forEach((card) => {
        card.classList.toggle(
          'hide',
          key !== 'all' && card.dataset.category !== key
        );
      });
    });
  });
});
