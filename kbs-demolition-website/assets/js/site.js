const CONFIG = {
  company: 'KBS Commercial Demolition',
  phoneDisplay: '(207) 555-0124',
  phoneHref: 'tel:+12075550124',
  email: 'estimating@yourkbsdomain.com',
  quoteEndpoint: '' // Paste a Formspree endpoint or FormSubmit AJAX endpoint here to receive quote submissions.
};

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-company]').forEach(el => el.textContent = CONFIG.company);
  document.querySelectorAll('[data-phone]').forEach(el => { el.textContent = CONFIG.phoneDisplay; el.href = CONFIG.phoneHref; });
  document.querySelectorAll('[data-email]').forEach(el => { el.textContent = CONFIG.email; el.href = `mailto:${CONFIG.email}`; });
  document.querySelectorAll('img[data-fallback]').forEach(img => img.addEventListener('error', () => { img.src = img.dataset.fallback; }));

  const toggle = document.querySelector('.menu-toggle'); const nav = document.querySelector('.nav-links');
  if(toggle && nav){toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded', String(open));});}

  const filters = document.querySelectorAll('[data-filter]');
  filters.forEach(button => button.addEventListener('click', () => {
    filters.forEach(b => b.classList.remove('active')); button.classList.add('active');
    const key = button.dataset.filter;
    document.querySelectorAll('.project').forEach(card => card.classList.toggle('hide', key !== 'all' && card.dataset.category !== key));
  }));

  const form = document.querySelector('[data-quote-form]');
  if(form){
    form.addEventListener('submit', async event => {
      event.preventDefault(); const status = form.querySelector('.status'); const submit = form.querySelector('button[type="submit"]');
      if(!CONFIG.quoteEndpoint){
        const details = [...new FormData(form).entries()].map(([k,v]) => `${k}: ${v}`).join('\n');
        const subject = encodeURIComponent('New KBS Commercial Demolition Quote Request');
        const body = encodeURIComponent(`A new quote request was submitted:\n\n${details}`);
        window.location.href = `mailto:${CONFIG.email}?subject=${subject}&body=${body}`;
        status.textContent = 'Your email app is opening with your quote request. To receive requests directly from the website, add your form endpoint in assets/js/site.js.';
        status.style.display='block';
        return;
      }
      try {
        submit.disabled=true; submit.textContent='Sending…';
        const res=await fetch(CONFIG.quoteEndpoint,{method:'POST',headers:{'Accept':'application/json'},body:new FormData(form)});
        if(!res.ok) throw new Error('Submission failed');
        form.reset(); status.textContent='Thank you — your quote request has been sent. Our estimating team will be in touch shortly.'; status.style.display='block';
      } catch(err) { status.textContent='We could not send this request. Please call or email us directly.'; status.style.display='block'; }
      finally { submit.disabled=false; submit.textContent='Request My Quote'; }
    });
  }
});
