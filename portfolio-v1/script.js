// ==========================================================================
// Interactive Behaviors & Animations (Matching Reference Video)
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

        // 1. ROCK-SOLID DYNAMIC TYPEWRITER (Zero Layout Shift, Perfect Stability)
    const typewriterElement = document.getElementById('typewriter');
    if (typewriterElement) {
        const words = [
            "Software",
            "Web Applications",
            "Custom Systems",
            "AI Automations",
            "Digital Platforms"
        ];
        let wordIndex = 0;
        let charIndex = words[0].length;
        let isDeleting = false;
        let typingSpeed = 90;

        function type() {
            const currentWord = words[wordIndex];

            if (isDeleting) {
                typewriterElement.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 40; // snappy backspace
            } else {
                typewriterElement.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 90; // smooth letter by letter
            }

            if (!isDeleting && charIndex === currentWord.length) {
                typingSpeed = 2400; // Pause proudly for 2.4s to be read comfortably
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typingSpeed = 350; // pause before next word
            }

            setTimeout(type, typingSpeed);
        }

        // Start typing after initial load
        setTimeout(type, 1200);
    }

    // 1B. BADGE DYNAMIC TYPEWRITER EFFECT
    const badgeElement = document.getElementById('badgeTypewriter');
    if (badgeElement) {
        const textToType = "FULL-STACK WEB & SOFTWARE DEVELOPER";
        let charIndex = 0;
        let isDeleting = false;
        let typingSpeed = 80;

        // Clear initial text so it types out letter-by-letter on load
        badgeElement.textContent = "";

        function typeBadge() {
            if (isDeleting) {
                badgeElement.textContent = textToType.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 35; // fast delete
            } else {
                badgeElement.textContent = textToType.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 80; // smooth letter by letter typing
            }

            if (!isDeleting && charIndex === textToType.length) {
                typingSpeed = 2600; // Pause when full text is revealed (কিছুক্ষণ দাঁড়িয়ে থাকবে)
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                typingSpeed = 500; // Pause before typing again
            }

            setTimeout(typeBadge, typingSpeed);
        }

        // Start typing after brief delay
        setTimeout(typeBadge, 400);
    }

    // 2. SCROLL REVEAL ANIMATIONS (IntersectionObserver)
    const revealElements = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        // Fallback for older browsers
        revealElements.forEach(el => el.classList.add('active'));
    }

    // 3. ANIMATED SKILLS PROGRESS BARS & NUMBERS
    const skillsSection = document.getElementById('skills');
    const skillCards = document.querySelectorAll('.skill-card');
    let animatedSkills = false;

    // Initially prepare bars and percents
    skillCards.forEach(card => {
        const bar = card.querySelector('.skill-bar-fill');
        const percentSpan = card.querySelector('.skill-percent');
        if (bar && percentSpan) {
            const targetVal = parseInt(percentSpan.textContent) || 90;
            bar.dataset.target = targetVal + '%';
            bar.style.width = '0%';
            percentSpan.dataset.target = targetVal;
            percentSpan.textContent = '0%';
        }
    });

    function animateSkillNumbers() {
        skillCards.forEach(card => {
            const bar = card.querySelector('.skill-bar-fill');
            const percentSpan = card.querySelector('.skill-percent');
            if (!bar || !percentSpan) return;

            bar.style.width = bar.dataset.target;
            const target = parseInt(percentSpan.dataset.target) || 90;
            const duration = 1400;
            const startTime = performance.now();

            function updateCounter(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                // easeOutQuad
                const currentVal = Math.round(target * (1 - (1 - progress) * (1 - progress)));
                percentSpan.textContent = currentVal + '%';

                if (progress < 1) {
                    requestAnimationFrame(updateCounter);
                } else {
                    percentSpan.textContent = target + '%';
                }
            }
            requestAnimationFrame(updateCounter);
        });
    }

    if (skillsSection && 'IntersectionObserver' in window) {
        const skillsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !animatedSkills) {
                    animatedSkills = true;
                    animateSkillNumbers();
                }
            });
        }, { threshold: 0.2 });

        skillsObserver.observe(skillsSection);
    } else {
        animateSkillNumbers();
    }

    // 4. MOBILE MENU TOGGLE
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('mobile-open');
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('mobile-open');
            });
        });
    }

    // ==========================================================================
    // 5. SMOOTH SCROLL ROUTER & REAL-TIME SCROLLSPY
    // "আমি যেন স্ক্রল করলে নিচের দিকে সবগুলা অপশন আসে, স্ক্রল করলে।"
    // ==========================================================================
    const navItems = document.querySelectorAll('.nav-links .nav-item');
    const sections = document.querySelectorAll('section[id]');
    const navbar = document.querySelector('.navbar');

    function getNavHeight() {
        return navbar ? navbar.offsetHeight : 70;
    }

    function scrollToSection(targetId) {
        if (!targetId) return;

        if (targetId === 'home') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            return;
        }

        const targetEl = document.getElementById(targetId) || document.getElementById('page-' + targetId);
        if (targetEl) {
            const navH = getNavHeight();
            const topPos = targetEl.getBoundingClientRect().top + window.pageYOffset - navH - 12;
            window.scrollTo({
                top: Math.max(0, topPos),
                behavior: 'smooth'
            });
        }
    }

    // Intercept clicks on navbar items, CTA buttons, and internal anchor links
    document.addEventListener('click', (e) => {
        const link = e.target.closest('a[href^="#"]');
        if (!link) return;

        const href = link.getAttribute('href');
        if (!href || href === '#') return;

        const targetId = href.replace('#', '').toLowerCase();
        const targetSection = document.getElementById(targetId) || document.getElementById('page-' + targetId);

        if (targetSection) {
            e.preventDefault();
            scrollToSection(targetId);

            // Close mobile menu if open
            if (navLinks && navLinks.classList.contains('mobile-open')) {
                navLinks.classList.remove('mobile-open');
            }

            // Update URL hash cleanly
            if (history.replaceState) {
                history.replaceState(null, null, '#' + targetId);
            }
        }
    });

    // Scroll Down indicator on Home smooth-scrolls cleanly to About section
    const scrollDownIndicator = document.querySelector('.scroll-down-indicator');
    if (scrollDownIndicator) {
        scrollDownIndicator.style.cursor = 'pointer';
        scrollDownIndicator.addEventListener('click', (e) => {
            e.preventDefault();
            scrollToSection('about');
        });
    }

    // Real-Time ScrollSpy: highlight active nav item as user scrolls down
    function updateActiveNavOnScroll() {
        const scrollY = window.pageYOffset;
        const navH = getNavHeight();
        let currentSectionId = 'home';

        if (scrollY > 120) {
            sections.forEach(section => {
                const sectionTop = section.offsetTop - navH - 60;
                const sectionHeight = section.offsetHeight;
                const id = section.getAttribute('id');
                if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                    currentSectionId = id;
                }
            });

            // If scrolled to bottom of page, activate contact
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 80) {
                currentSectionId = 'contact';
            }
        }

        navItems.forEach(item => {
            const href = item.getAttribute('href');
            if (href === '#' + currentSectionId) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    }

    window.addEventListener('scroll', updateActiveNavOnScroll, { passive: true });

    // Handle initial load based on URL hash (e.g. #about, #projects)
    if (window.location.hash) {
        const initialTarget = window.location.hash.replace('#', '').toLowerCase();
        setTimeout(() => {
            scrollToSection(initialTarget);
        }, 150);
    }

    // 6. CONTACT FORM: DUAL DISPATCH (SERVER DATABASE + WHATSAPP INSTANT CHAT)
    const contactForm = document.getElementById('contactForm');
    const toast = document.getElementById('toast');
    const contactSubmitBtn = document.getElementById('contactSubmitBtn');

    if (contactForm && toast) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const nameInput = document.getElementById('contactName');
            const emailInput = document.getElementById('contactEmail');
            const messageInput = document.getElementById('contactMessage');

            const name = nameInput ? nameInput.value.trim() : '';
            const email = emailInput ? emailInput.value.trim() : '';
            const message = messageInput ? messageInput.value.trim() : '';

            if (!name || !message) return;

            // Button visual feedback
            if (contactSubmitBtn) {
                contactSubmitBtn.disabled = true;
                contactSubmitBtn.textContent = 'Sending...';
            }

            try {
                // 1. Save permanently to Server Database (data/messages.json)
                await fetch('/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, email, message })
                });
            } catch (err) {
                console.warn('Server message backup notice:', err);
            }

            // 2. Open WhatsApp directly pre-filled with the client message
            const waText = encodeURIComponent(
                `Assalamu Alaikum Miraz,

Name: ${name}
Email: ${email}

Project Details:
${message}`
            );
            const waUrl = `https://wa.me/8801339564967?text=${waText}`;

            // Open WhatsApp in a new tab so client can send immediately
            window.open(waUrl, '_blank');

            // 3. User feedback
            toast.textContent = "Thank you! Your message has been saved and forwarded to WhatsApp.";
            toast.classList.add('show');
            contactForm.reset();

            if (contactSubmitBtn) {
                contactSubmitBtn.disabled = false;
                contactSubmitBtn.innerHTML = 'Send Message <span class="arrow">→</span>';
            }

            setTimeout(() => {
                toast.classList.remove('show');
            }, 4000);
        });
    }

    // 7. REAL CV PDF DOWNLOAD & NOTIFICATION
    document.querySelectorAll('.nav-cv-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Allow natural browser download or trigger programmatically
            const downloadLink = document.createElement('a');
            downloadLink.href = 'Merajul_Islam_CV.pdf';
            downloadLink.download = 'Merajul_Islam_CV.pdf';
            downloadLink.target = '_blank';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);

            if (toast) {
                toast.textContent = "📄 Downloading Merajul Islam (Miraz) Official CV / Resume...";
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 3500);
            }
        });
    });

    // 8. PROJECT CATEGORY FILTER & CARD PREVIEWS
    const projectFilterBtns = document.querySelectorAll('.project-filter-btn');
    const allProjectCards = document.querySelectorAll('.project-card');

    if (projectFilterBtns.length > 0) {
        projectFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                projectFilterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');

                allProjectCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filter === 'all' || category === filter) {
                        card.style.display = 'flex';
                        requestAnimationFrame(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        });
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(12px)';
                        setTimeout(() => {
                            if (!card.classList.contains('active-show')) {
                                card.style.display = 'none';
                            }
                        }, 250);
                    }
                });
            });
        });
    }

    allProjectCards.forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('a') || e.target.closest('button')) return;
            const primaryLink = card.querySelector('.btn-live')?.href || card.querySelector('.btn-code')?.href;
            if (primaryLink) {
                window.open(primaryLink, '_blank', 'noopener,noreferrer');
            }
        });
    });

    
    // 9. PINTEREST MOON VIDEO AUDIO TOGGLE
    const moonVideo = document.getElementById('moonMediaVideo');
    const moonSoundBtn = document.getElementById('moonSoundBtn');
    const soundIcon = document.getElementById('soundIcon');

    if (moonVideo && moonSoundBtn && soundIcon) {
        moonSoundBtn.addEventListener('click', () => {
            moonVideo.muted = !moonVideo.muted;
            if (moonVideo.muted) {
                soundIcon.textContent = '🔇';
                moonSoundBtn.title = 'Unmute Video';
            } else {
                soundIcon.textContent = '🔊';
                moonSoundBtn.title = 'Mute Video';
                moonVideo.play().catch(() => {});
            }
        });
    }

    
    // 9. LUNAR BACKGROUND VIDEO AUDIO TOGGLE
    const lunarBgVideo = document.getElementById('lunarBgVideo');
    const lunarSoundBtn = document.getElementById('lunarSoundBtn');
    const lunarSoundIcon = document.getElementById('lunarSoundIcon');

    if (lunarBgVideo && lunarSoundBtn && lunarSoundIcon) {
        lunarSoundBtn.addEventListener('click', () => {
            lunarBgVideo.muted = !lunarBgVideo.muted;
            if (lunarBgVideo.muted) {
                lunarSoundIcon.textContent = '🔇';
                lunarSoundBtn.title = 'Unmute Moonlight Audio';
            } else {
                lunarSoundIcon.textContent = '🔊';
                lunarSoundBtn.title = 'Mute Moonlight Audio';
                lunarBgVideo.play().catch(() => {});
            }
        });
    }

    // 9b. LUNAR SMOKE & EMBERS VIDEO AUTOPLAY
    const lunarSmokeVideo = document.getElementById('lunarSmokeVideo');
    if (lunarSmokeVideo) {
        lunarSmokeVideo.play().catch(() => {});
        ['click', 'touchstart', 'scroll'].forEach(evt => {
            window.addEventListener(evt, () => {
                if (lunarSmokeVideo && lunarSmokeVideo.paused) {
                    lunarSmokeVideo.play().catch(() => {});
                }
            }, { once: true, passive: true });
        });
    }

    
    // 10. SITE ENTRY LOGO INTRO ANIMATION DISMISSAL
    const introOverlay = document.getElementById('siteIntroOverlay');
    if (introOverlay) {
        function dismissIntro() {
            introOverlay.classList.add('fade-out');
            setTimeout(() => {
                introOverlay.style.display = 'none';
            }, 600);
        }

        // Dismiss smoothly after 1.15 seconds
        setTimeout(dismissIntro, 1150);

        // Or dismiss immediately on click
        introOverlay.addEventListener('click', dismissIntro);
    }

    
    // ==========================================================================
    // 11. INTERACTIVE RISING SMOKE & EMBER BURST ON CLICK (Pure Smoke, Zero Candle)
    // "যখন আমি ক্লিক বেশি করবো তখন ধোঁয়াটা বাড়বে। আর এমনি স্বাভাবিকভাবে ধোঁয়া বের হবে।"
    // ==========================================================================
    (function initInteractiveSmoke() {
        const canvas = document.getElementById('heroSmokeCanvas');
        const heroSection = document.getElementById('home');
        const smokeVideo = document.getElementById('heroSmokeVideo');
        if (!canvas || !heroSection) return;

        const ctx = canvas.getContext('2d');
        let width = 0;
        let height = 0;
        let dpr = Math.min(window.devicePixelRatio || 1, 2);

        function resize() {
            const rect = heroSection.getBoundingClientRect();
            width = rect.width;
            height = rect.height;
            canvas.width = Math.floor(width * dpr);
            canvas.height = Math.floor(height * dpr);
            canvas.style.width = width + 'px';
            canvas.style.height = height + 'px';
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        }
        resize();
        window.addEventListener('resize', resize);

        const smokeParticles = [];
        const emberParticles = [];
        let videoIntensity = 0; // 0 (calm ambient) to 1.0 (intense billowing)

        // Realistic Rising Smoke Particle with organic billowing & dissipation
        class SmokeParticle {
            constructor(x, y, isClick = false) {
                this.x = x + (Math.random() - 0.5) * (isClick ? 40 : width * 0.7);
                this.y = y + (Math.random() - 0.5) * 20;
                this.radius = isClick ? (Math.random() * 28 + 22) : (Math.random() * 38 + 32);
                this.maxRadius = this.radius * (isClick ? (Math.random() * 3.8 + 3.2) : (Math.random() * 3.2 + 2.6));
                this.growth = (this.maxRadius - this.radius) / (isClick ? (Math.random() * 85 + 85) : 170);
                this.vy = isClick ? -(Math.random() * 2.4 + 1.6) : -(Math.random() * 1.0 + 0.55);
                this.vx = (Math.random() - 0.5) * (isClick ? 1.4 : 0.6);
                this.swaySpeed = Math.random() * 0.025 + 0.012;
                this.swayOffset = Math.random() * Math.PI * 2;
                this.life = 0;
                this.maxLife = isClick ? (Math.random() * 110 + 95) : (Math.random() * 170 + 130);
                this.maxAlpha = isClick ? (Math.random() * 0.30 + 0.22) : (Math.random() * 0.14 + 0.08);
                this.alpha = 0;

                // Subtle candle flame smoke color palette (creamy grey & warm embers tint)
                const isWarm = Math.random() < 0.4;
                this.colorR = isWarm ? 245 : 210;
                this.colorG = isWarm ? 200 : 215;
                this.colorB = isWarm ? 185 : 230;
            }

            update() {
                this.life++;
                this.radius += this.growth;
                this.y += this.vy;
                this.x += this.vx + Math.sin(this.life * this.swaySpeed + this.swayOffset) * 0.5;

                // Smooth bell-curve alpha fade: rises gracefully, lingers, then evaporates
                const progress = this.life / this.maxLife;
                if (progress < 0.18) {
                    this.alpha = (progress / 0.18) * this.maxAlpha;
                } else {
                    this.alpha = (1 - (progress - 0.18) / 0.82) * this.maxAlpha;
                }

                return this.life < this.maxLife && (this.y + this.radius) > -50;
            }

            draw(ctx) {
                if (this.alpha <= 0.005) return;
                const grad = ctx.createRadialGradient(
                    this.x, this.y, 0,
                    this.x, this.y, this.radius
                );
                grad.addColorStop(0, `rgba(${this.colorR}, ${this.colorG}, ${this.colorB}, ${this.alpha})`);
                grad.addColorStop(0.35, `rgba(${this.colorR - 15}, ${this.colorG - 15}, ${this.colorB - 15}, ${this.alpha * 0.55})`);
                grad.addColorStop(0.70, `rgba(110, 110, 125, ${this.alpha * 0.22})`);
                grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

                ctx.fillStyle = grad;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // Sparkling Fire Ember Particle (Golden-Red glow ascending with wind turbulence)
        class EmberParticle {
            constructor(x, y, isClick = false) {
                this.x = x + (Math.random() - 0.5) * (isClick ? 45 : width * 0.6);
                this.y = y + (Math.random() - 0.5) * 20;
                this.radius = Math.random() * 2.0 + 0.8;
                this.vy = isClick ? -(Math.random() * 3.8 + 2.0) : -(Math.random() * 1.6 + 0.9);
                this.vx = (Math.random() - 0.5) * (isClick ? 2.4 : 0.9);
                this.life = 0;
                this.maxLife = isClick ? (Math.random() * 85 + 75) : (Math.random() * 125 + 90);
                this.alpha = 1;

                // Rich crimson and golden ember hues
                const isGold = Math.random() < 0.45;
                const hue = isGold ? (Math.random() * 20 + 38) : (Math.random() * 25 + 5);
                this.color = `hsl(${hue}, 100%, ${Math.random() * 25 + 55}%)`;
            }

            update() {
                this.life++;
                this.y += this.vy;
                this.x += this.vx + Math.sin(this.life * 0.08) * 0.65;
                this.alpha = Math.max(0, 1 - (this.life / this.maxLife));
                return this.life < this.maxLife && this.y > -20;
            }

            draw(ctx) {
                if (this.alpha <= 0.01) return;
                ctx.save();
                ctx.globalAlpha = this.alpha;
                ctx.shadowColor = '#FF2A3B';
                ctx.shadowBlur = 9;
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }

        // Spawns rich smoke and ember bursts when user clicks or taps
        function triggerBurst(clientX, clientY) {
            const rect = heroSection.getBoundingClientRect();
            let targetX = clientX - rect.left;
            let targetY = clientY - rect.top;

            targetX = Math.max(30, Math.min(width - 30, targetX));
            targetY = Math.max(40, Math.min(height - 10, targetY));

            // Increase background smoke video glow and opacity smoothly
            videoIntensity = Math.min(1.0, videoIntensity + 0.38);

            // Click particle burst count
            const smokeCount = Math.floor(Math.random() * 6 + 12); // 12-17 smoke clouds
            const emberCount = Math.floor(Math.random() * 8 + 14); // 14-21 sparkling embers

            for (let i = 0; i < smokeCount; i++) {
                smokeParticles.push(new SmokeParticle(targetX, targetY, true));
            }
            for (let i = 0; i < emberCount; i++) {
                emberParticles.push(new EmberParticle(targetX, targetY, true));
            }

            // Upward surging plume from base beneath click position
            for (let i = 0; i < 5; i++) {
                smokeParticles.push(new SmokeParticle(targetX + (Math.random() - 0.5) * 60, height - 15, true));
                emberParticles.push(new EmberParticle(targetX + (Math.random() - 0.5) * 50, height - 15, true));
            }
        }

        // Desktop Click Listener on Hero Section
        heroSection.addEventListener('click', (e) => {
            triggerBurst(e.clientX, e.clientY);
        });

        // Mobile Touch Listener on Hero Section
        heroSection.addEventListener('touchstart', (e) => {
            if (e.touches && e.touches.length > 0) {
                triggerBurst(e.touches[0].clientX, e.touches[0].clientY);
            }
        }, { passive: true });

        // Animation Loop: Ambient Flow + Interactive Billowing
        let ambientTimer = 0;
        function renderLoop() {
            ctx.clearRect(0, 0, width, height);

            // Ambient gentle smoke flow (normal idle state - "এমনি হালকা স্বাভাবিকভাবে ধোঁয়া বের হবে")
            ambientTimer++;
            if (ambientTimer % 32 === 0 && smokeParticles.length < 45) {
                const ambientX = width * 0.5 + (Math.random() - 0.5) * (width * 0.75);
                smokeParticles.push(new SmokeParticle(ambientX, height - 20, false));
            }
            if (ambientTimer % 26 === 0 && emberParticles.length < 35) {
                const ambientX = width * 0.5 + (Math.random() - 0.5) * (width * 0.70);
                emberParticles.push(new EmberParticle(ambientX, height - 20, false));
            }

            // Smooth background video intensity decay back to calm ambient
            if (videoIntensity > 0) {
                videoIntensity = Math.max(0, videoIntensity - 0.007);
                if (smokeVideo) {
                    smokeVideo.style.opacity = (0.58 + videoIntensity * 0.38).toFixed(2);
                    smokeVideo.style.filter = `brightness(${(1.10 + videoIntensity * 0.30).toFixed(2)}) contrast(${(1.15 + videoIntensity * 0.15).toFixed(2)})`;
                }
            } else if (smokeVideo && smokeVideo.style.opacity !== '0.58') {
                smokeVideo.style.opacity = '0.58';
                smokeVideo.style.filter = 'brightness(1.10) contrast(1.15)';
            }

            // Update & draw smoke clouds
            for (let i = smokeParticles.length - 1; i >= 0; i--) {
                const p = smokeParticles[i];
                if (p.update()) {
                    p.draw(ctx);
                } else {
                    smokeParticles.splice(i, 1);
                }
            }

            // Update & draw sparkling embers
            for (let i = emberParticles.length - 1; i >= 0; i--) {
                const p = emberParticles[i];
                if (p.update()) {
                    p.draw(ctx);
                } else {
                    emberParticles.splice(i, 1);
                }
            }

            requestAnimationFrame(renderLoop);
        }

        requestAnimationFrame(renderLoop);
    })();

    // ==========================================================================
    // 8. INTERACTIVE CLIENT TESTIMONIALS & REVIEWS SYSTEM
    // ==========================================================================
    const testimonialsGrid = document.getElementById('testimonialsGrid');
    const reviewModal = document.getElementById('reviewModal');
    const openReviewModalBtn = document.getElementById('openReviewModalBtn');
    const closeReviewModalBtn = document.getElementById('closeReviewModalBtn');
    const cancelReviewBtn = document.getElementById('cancelReviewBtn');
    const clientReviewForm = document.getElementById('clientReviewForm');
    const starBtns = document.querySelectorAll('.star-btn');
    const ratingInput = document.getElementById('reviewRatingInput');
    const starRatingLabel = document.getElementById('starRatingLabel');

    const ratingLabels = {
        1: '1.0 / 5.0 (Poor)',
        2: '2.0 / 5.0 (Fair)',
        3: '3.0 / 5.0 (Good)',
        4: '4.0 / 5.0 (Very Good)',
        5: '5.0 / 5.0 (Exceptional)'
    };

    function renderStars(rating) {
        let stars = '';
        const count = Math.max(1, Math.min(5, parseInt(rating, 10) || 5));
        for (let i = 0; i < count; i++) {
            stars += '★';
        }
        return stars;
    }

    function escapeHTML(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function createReviewCardHTML(rev) {
        const stars = renderStars(rev.rating);
        const avatarUrl = rev.avatar || `https://api.dicebear.com/7.x/initials/svg?seed=${encodeURIComponent(rev.name)}&backgroundColor=FF2A3B&textColor=ffffff`;
        const role = rev.role || 'Verified Client';

        return `
            <div class="testimonial-card reveal active" data-id="${rev.id || ''}">
                <div class="quote-mark">“</div>
                <p class="testimonial-quote">
                    ${escapeHTML(rev.review)}
                </p>
                <div class="testimonial-footer">
                    <img src="${avatarUrl}" alt="${escapeHTML(rev.name)}" class="client-avatar" onerror="this.src='images/testimonial_daniel.png'">
                    <div class="client-info">
                        <h5 class="client-name">${escapeHTML(rev.name)}</h5>
                        <p class="client-role">${escapeHTML(role)}</p>
                    </div>
                </div>
                <div class="rating-stars">${stars}</div>
            </div>
        `;
    }

    async function loadTestimonials() {
        if (!testimonialsGrid) return;
        try {
            const res = await fetch('/api/reviews');
            if (res.ok) {
                const reviews = await res.json();
                if (Array.isArray(reviews) && reviews.length > 0) {
                    testimonialsGrid.innerHTML = reviews.map(createReviewCardHTML).join('');
                    return;
                }
            }
        } catch (e) {
            console.log('Using offline reviews fallback');
        }

        const local = localStorage.getItem('miraz_portfolio_reviews');
        if (local) {
            try {
                const reviews = JSON.parse(local);
                if (Array.isArray(reviews) && reviews.length > 0) {
                    testimonialsGrid.innerHTML = reviews.map(createReviewCardHTML).join('');
                }
            } catch (err) {}
        }
    }

    function openModal() {
        if (reviewModal) {
            reviewModal.classList.add('active');
            reviewModal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
            const firstInput = document.getElementById('reviewClientName');
            if (firstInput) setTimeout(() => firstInput.focus(), 100);
        }
    }

    function closeModal() {
        if (reviewModal) {
            reviewModal.classList.remove('active');
            reviewModal.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }

    if (openReviewModalBtn) openReviewModalBtn.addEventListener('click', openModal);
    if (closeReviewModalBtn) closeReviewModalBtn.addEventListener('click', closeModal);
    if (cancelReviewBtn) cancelReviewBtn.addEventListener('click', closeModal);

    if (reviewModal) {
        reviewModal.addEventListener('click', (e) => {
            if (e.target === reviewModal) closeModal();
        });
    }

    function setRating(val) {
        const rating = Math.max(1, Math.min(5, val));
        if (ratingInput) ratingInput.value = rating;
        if (starRatingLabel) starRatingLabel.textContent = ratingLabels[rating] || (rating + '.0 / 5.0');
        starBtns.forEach(btn => {
            const btnVal = parseInt(btn.dataset.rating, 10);
            if (btnVal <= rating) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    starBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const val = parseInt(btn.dataset.rating, 10);
            setRating(val);
        });
        btn.addEventListener('mouseenter', () => {
            const hoverVal = parseInt(btn.dataset.rating, 10);
            starBtns.forEach(b => {
                const bVal = parseInt(b.dataset.rating, 10);
                if (bVal <= hoverVal) {
                    b.classList.add('hover');
                } else {
                    b.classList.remove('hover');
                }
            });
        });
    });

    const selectorBox = document.getElementById('starRatingSelector');
    if (selectorBox) {
        selectorBox.addEventListener('mouseleave', () => {
            starBtns.forEach(b => b.classList.remove('hover'));
        });
    }

    if (clientReviewForm) {
        clientReviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('submitReviewBtn');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span>Submitting... ⏳</span>';
            }

            const name = document.getElementById('reviewClientName')?.value.trim();
            const role = document.getElementById('reviewClientRole')?.value.trim() || 'Verified Client';
            const review = document.getElementById('reviewMessage')?.value.trim();
            const rating = parseInt(ratingInput?.value, 10) || 5;

            const newReviewObj = {
                name,
                role,
                review,
                rating,
                avatar: `https://api.dicebear.com/7.x/initials/svg?seed=${encodeURIComponent(name)}&backgroundColor=FF2A3B&textColor=ffffff`,
                date: new Date().toISOString().split('T')[0]
            };

            try {
                const res = await fetch('/api/reviews', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(newReviewObj)
                });
                if (res.ok) {
                    const data = await res.json();
                    if (data.review) {
                        newReviewObj.id = data.review.id;
                    }
                }
            } catch (err) {
                console.log('Network error on submit, saving locally');
            }

            try {
                const currentLocal = JSON.parse(localStorage.getItem('miraz_portfolio_reviews') || '[]');
                currentLocal.unshift(newReviewObj);
                localStorage.setItem('miraz_portfolio_reviews', JSON.stringify(currentLocal));
            } catch (err) {}

            if (testimonialsGrid) {
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = createReviewCardHTML(newReviewObj);
                const newCard = tempDiv.firstElementChild;
                if (newCard) {
                    newCard.style.border = '1.5px solid #FF2A3B';
                    newCard.style.boxShadow = '0 0 20px rgba(255, 42, 59, 0.35)';
                    testimonialsGrid.prepend(newCard);
                }
            }

            closeModal();
            clientReviewForm.reset();
            setRating(5);

            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<span>Submit Review 🚀</span>';
            }

            const toast = document.getElementById('toast');
            if (toast) {
                toast.textContent = "🎉 Thank you! Your review has been saved & published.";
                toast.classList.add('show');
                setTimeout(() => toast.classList.remove('show'), 4000);
            }
        });
    }

    loadTestimonials();


    console.log('Portfolio with dynamic typewriter & animations initialized.');
});




