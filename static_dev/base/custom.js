// Scroll to top button visibility
window.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('scrollTop');
  if (!btn) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
      btn.classList.remove('d-none');
    } else {
      btn.classList.add('d-none');
    }
  });
});

