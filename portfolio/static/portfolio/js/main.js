// Mobile nav toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  // Close nav when a link is clicked
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
    });
  });
}

// Animate skill bars on scroll
const skillBars = document.querySelectorAll('.skill-bar-fill');

const animateBars = (entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.width = entry.target.dataset.width || entry.target.style.width;
      observer.unobserve(entry.target);
    }
  });
};

if ('IntersectionObserver' in window) {
  const barObserver = new IntersectionObserver(animateBars, { threshold: 0.3 });

  skillBars.forEach(bar => {
    const targetWidth = bar.style.width;
    bar.dataset.width = targetWidth;
    bar.style.width = '0%';
    barObserver.observe(bar);
  });
}

// Highlight active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a');

const highlightNav = () => {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 80;
    if (window.scrollY >= sectionTop) {
      current = section.getAttribute('id');
    }
  });

  navAnchors.forEach(a => {
    a.style.color = '';
    if (a.getAttribute('href') === '#' + current) {
      a.style.color = 'var(--accent)';
    }
  });
};

window.addEventListener('scroll', highlightNav, { passive: true });

// Auto-dismiss flash messages
const flashes = document.querySelectorAll('.flash');
flashes.forEach(flash => {
  setTimeout(() => {
    flash.style.transition = 'opacity 0.5s';
    flash.style.opacity = '0';
    setTimeout(() => flash.remove(), 500);
  }, 4000);
});
