document.addEventListener("DOMContentLoaded", function() {
    // Mobile menu toggle
    const menuBtn = document.getElementById("menuBtn");
    const mobileMenu = document.getElementById("mobileMenu");

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener("click", () => {
            const isHidden = mobileMenu.classList.toggle("hidden");
            const expanded = !isHidden;
            menuBtn.setAttribute("aria-expanded", expanded.toString());
        });

        // Keyboard accessibility for menu
        menuBtn.addEventListener("keydown", (e) => {
            if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                menuBtn.click();
            }
        });
    } else {
        console.warn("Menu button or mobile menu not found");
    }

    // Typing animation for "Hello, my name is" on index.html
    const indexTextElement = document.getElementById('typing-text');
    if (indexTextElement) {
        initializeTypingAnimation(indexTextElement, "Hello, my name is");
    } else {
        console.warn("Typing text element not found on this page");
    }

    // Typing animation for "A little about me" on about.html
    const aboutTextElement = document.getElementById('about-typing-text');
    if (aboutTextElement) {
        initializeTypingAnimation(aboutTextElement, "A little about me");
    } else {
        console.warn("About typing text element not found on this page");
    }

    function initializeTypingAnimation(element, text) {
        if (!element) return;
        let index = 0;
        let isDeleting = false;
        function typeWriter() {
            let currentText = text.substring(0, index);
            element.textContent = currentText;
            if (!isDeleting && index <= text.length) {
                index++;
            } else if (isDeleting && index >= 0) {
                index--;
            }
            if (index === text.length + 1) {
                isDeleting = true;
            }
            if (index === 0 && isDeleting) {
                isDeleting = false;
            }
            let typingSpeed = 100;
            if (isDeleting) {
                typingSpeed = 50;
            }
            setTimeout(typeWriter, typingSpeed);
        }
        typeWriter();
    }

    // Carousel functionality
    let slideTimers = {};

    function changeSlide(sliderId, n) {
        const slider = document.getElementById(sliderId);
        if (!slider) {
            console.warn(`Slider ${sliderId} not found`);
            return;
        }

        const slides = Array.from(slider.children);
        if (slides.length === 0) {
            console.warn(`No slides found in ${sliderId}`);
            return;
        }

        let currentIndex = parseInt(slider.style.transform.replace('translateX(-', '').replace('%)', '')) / 100 || 0;
        let totalSlides = slides.length;
        let newIndex = (currentIndex + n + totalSlides) % totalSlides;
        slider.style.transform = `translateX(-${newIndex * 100}%)`;
        updateDots(sliderId, newIndex);
    }

    function autoSlide(sliderId) {
        const slider = document.getElementById(sliderId);
        if (slider) {
            slider.classList.add('loading');
            setTimeout(() => {
                changeSlide(sliderId, 1);
                slider.classList.remove('loading');
            }, 500);
        }
    }

    function restartAutoSlide(sliderId) {
        const slider = document.getElementById(sliderId);
        if (!slider) return;
        clearInterval(slideTimers[sliderId]);
        slideTimers[sliderId] = setInterval(() => autoSlide(sliderId), 3000); // Auto-slide every 3 seconds
    }

    function updateDots(sliderId, index) {
        const dots = document.querySelectorAll(`#${sliderId} + * + .absolute.bottom-2 .bg-gray-400, .bg-purple-400`);
        if (dots.length > 0) {
            dots.forEach(dot => dot.classList.remove('bg-purple-400'));
            dots[index].classList.add('bg-purple-400');
        }
    }

    function setupSlider(sliderId) {
        const slider = document.getElementById(sliderId);
        if (!slider) return;

        const slides = Array.from(slider.children);
        const totalSlides = slides.length;
        const prevBtn = document.getElementById(`${sliderId}-prev`);
        const nextBtn = document.getElementById(`${sliderId}-next`);
        const dots = document.querySelectorAll(`#${sliderId} + * + .absolute.bottom-2 .bg-gray-400, .bg-purple-400`);

        if (totalSlides > 1 && prevBtn && nextBtn) {
            prevBtn.addEventListener("click", () => changeSlide(sliderId, -1));
            nextBtn.addEventListener("click", () => changeSlide(sliderId, 1));

            dots.forEach(dot => {
                dot.addEventListener("click", () => {
                    const index = parseInt(dot.getAttribute("data-index"));
                    slider.style.transform = `translateX(-${index * 100}%)`;
                    updateDots(sliderId, index);
                });
            });
        }

        if (totalSlides > 1) {
            restartAutoSlide(sliderId); // Start auto-slide immediately
        }
    }

    // Carousel controls
    const expPrev = document.getElementById("exp-prev");
    const expNext = document.getElementById("exp-next");

    if (expPrev && expNext) {
        expPrev.addEventListener("click", () => changeSlide("exp-slider", -1));
        expNext.addEventListener("click", () => changeSlide("exp-slider", 1));
        restartAutoSlide("exp-slider");
    } else {
        console.warn("Carousel controls (exp-prev, exp-next) not found");
    }

    const projectSliders = document.querySelectorAll('.project-slider-inner');
    projectSliders.forEach(slider => {
        setupSlider(slider.id);
    });

    // Bubble animations
    const bubbleObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const row = entry.target;
                const cards = row.querySelectorAll('.project-card');
                if (cards.length > 0) {
                    cards.forEach(card => {
                        const order = parseInt(card.dataset.animationOrder, 10) || 1;
                        const delay = (order - 1) * 200;
                        setTimeout(() => {
                            card.classList.add('bubble-card');
                        }, delay);
                    });
                    bubbleObserver.unobserve(row);
                } else {
                    console.warn("No project cards found in row");
                }
            }
        });
    }, {
        threshold: 0.5
    });

    const projectRows = document.querySelectorAll('.project-row');
    if (projectRows.length > 0) {
        projectRows.forEach(row => {
            bubbleObserver.observe(row);
        });
    } else {
        console.warn("No project rows found");
    }

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const href = this.getAttribute('href');
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            } else {
                console.warn(`Target ${href} not found for smooth scroll`);
            }
        });
    });
});