// Mobile Navigation Toggle
const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
const navbar = document.getElementById('navbar');

mobileNavToggle.addEventListener('click', () => {
    navbar.classList.toggle('active');
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            if (navbar.classList.contains('active')) {
                navbar.classList.remove('active');
            }
        }
    });
});

// Testimonials Slider
const testimonialsContainer = document.getElementById('testimonials-container');
const dots = document.querySelectorAll('.dot');
let currentIndex = 0;

function showTestimonial(index) {
    testimonialsContainer.style.transform = `translateX(-${index * 100}%)`;
    
    // Update active dot
    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
    
    currentIndex = index;
}

// Dot navigation
dots.forEach(dot => {
    dot.addEventListener('click', function() {
        const index = parseInt(this.getAttribute('data-index'));
        showTestimonial(index);
    });
});

// Auto slide testimonials
setInterval(() => {
    currentIndex = (currentIndex + 1) % dots.length;
    showTestimonial(currentIndex);
}, 5000);

// Form submission
const bookingForm = document.getElementById('booking-form');

bookingForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        service: document.getElementById('service').value,
        date: document.getElementById('date').value,
        message: document.getElementById('message').value
    };

    try {
        const response = await fetch('/api/book-appointment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (response.ok) {
            alert('Thank you for your booking request! We will contact you shortly to confirm your appointment.');
            bookingForm.reset();
        } else {
            alert('Error: ' + data.message);
        }
    } catch (error) {
        alert('An error occurred while submitting the form. Please try again later.');
        console.error('Error:', error);
    }
});

// Add animation class to elements when they come into view
const animateOnScroll = function() {
    const serviceCards = document.querySelectorAll('.service-card');
    
    serviceCards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (cardTop < windowHeight * 0.8) {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }
    });
};

// Initialize service cards with opacity 0
document.querySelectorAll('.service-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
});

// Listen for scroll events
window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll); 