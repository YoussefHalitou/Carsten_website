// Sticky Header Scroll Effect
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Mobile Menu Toggle
function toggleMenu() {
    const navMenu = document.getElementById('navMenu');
    navMenu.classList.toggle('active');
}

// Mobile Menu Toggle
function toggleMenu() {
    const menu = document.getElementById('navMenu');
    const toggle = document.querySelector('.menu-toggle i');
    menu.classList.toggle('active');
    
    if (menu.classList.contains('active')) {
        toggle.classList.remove('fa-bars');
        toggle.classList.add('fa-times');
    } else {
        toggle.classList.remove('fa-times');
        toggle.classList.add('fa-bars');
    }
}

function closeMenu() {
    const menu = document.getElementById('navMenu');
    const toggle = document.querySelector('.menu-toggle i');
    menu.classList.remove('active');
    toggle.classList.remove('fa-times');
    toggle.classList.add('fa-bars');
}

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    const menu = document.getElementById('navMenu');
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');
    
    if (menu && nav && !nav.contains(event.target) && menu.classList.contains('active')) {
        closeMenu();
    }
});

// Close menu when clicking on a link
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function() {
        closeMenu();
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});





// Truncate article summaries
document.addEventListener('DOMContentLoaded', function() {
    const summaries = document.querySelectorAll('.article-content p');
    const maxLength = 150; // Zeichen
    
    summaries.forEach(summary => {
        const text = summary.textContent;
        if (text.length > maxLength) {
            summary.textContent = text.substring(0, maxLength) + '...';
        }
    });
});