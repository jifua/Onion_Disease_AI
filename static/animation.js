// =========================================================
// ONIONBOT AI PLATFORM
// ANIMATION ENGINE FINAL 3X
// =========================================================


// =========================================================
// PARTICLE ENGINE
// =========================================================

function createParticle() {

    const particle = document.createElement(

        "div"

    );

    particle.classList.add(

        "floating-particle"

    );

    document.body.appendChild(

        particle

    );

    const size =

        Math.random() * 8 + 4;

    particle.style.width =

        `${size}px`;

    particle.style.height =

        `${size}px`;

    particle.style.left =

        `${Math.random() * window.innerWidth}px`;

    particle.style.top =

        `${window.innerHeight + 20}px`;

    particle.style.opacity =

        Math.random();

    particle.style.animationDuration =

        `${Math.random() * 8 + 6}s`;

    setTimeout(() => {

        particle.remove();

    }, 12000);

}


// =========================================================
// AUTO PARTICLE LOOP
// =========================================================

setInterval(() => {

    createParticle();

}, 900);


// =========================================================
// HERO FLOAT EFFECT
// =========================================================

function heroFloatEffect() {

    const robot = document.querySelector(

        ".robot-container"

    );

    if (!robot) return;

    let direction = 1;

    setInterval(() => {

        robot.style.transform =

            `translateY(${direction * 10}px)`;

        direction *= -1;

    }, 2000);

}

heroFloatEffect();


// =========================================================
// CARD HOVER EFFECT
// =========================================================

function cardHoverEffect() {

    const cards = document.querySelectorAll(

        ".bot-card, .stats-card, .analytics-card"

    );

    cards.forEach(card => {

        card.addEventListener(

            "mousemove",

            (e) => {

                const rect =

                    card.getBoundingClientRect();

                const x =

                    e.clientX - rect.left;

                const y =

                    e.clientY - rect.top;

                const centerX =

                    rect.width / 2;

                const centerY =

                    rect.height / 2;

                const rotateX =

                    ((y - centerY) / 20);

                const rotateY =

                    ((centerX - x) / 20);

                card.style.transform =

                    `perspective(1000px)
                     rotateX(${rotateX}deg)
                     rotateY(${rotateY}deg)
                     translateY(-5px)`;

            }

        );

        card.addEventListener(

            "mouseleave",

            () => {

                card.style.transform =

                    `perspective(1000px)
                     rotateX(0deg)
                     rotateY(0deg)
                     translateY(0px)`;

            }

        );

    });

}

cardHoverEffect();


// =========================================================
// ONLINE STATUS EFFECT
// =========================================================

function onlinePulse() {

    const dots = document.querySelectorAll(

        ".online-dot, .activity-dot"

    );

    dots.forEach(dot => {

        dot.animate(

            [

                {

                    transform: "scale(1)",

                    opacity: 1

                },

                {

                    transform: "scale(1.4)",

                    opacity: 0.5

                },

                {

                    transform: "scale(1)",

                    opacity: 1

                }

            ],

            {

                duration: 1500,

                iterations: Infinity

            }

        );

    });

}

onlinePulse();


// =========================================================
// TYPING DOT EFFECT
// =========================================================

function typingEffect() {

    const dots = document.querySelectorAll(

        ".typing-animation span"

    );

    dots.forEach((dot, index) => {

        dot.animate(

            [

                {

                    transform: "translateY(0px)",

                    opacity: 0.4

                },

                {

                    transform: "translateY(-8px)",

                    opacity: 1

                },

                {

                    transform: "translateY(0px)",

                    opacity: 0.4

                }

            ],

            {

                duration: 900,

                delay: index * 180,

                iterations: Infinity

            }

        );

    });

}

typingEffect();


// =========================================================
// SMOOTH NAVBAR EFFECT
// =========================================================

window.addEventListener(

    "scroll",

    () => {

        const navbar = document.querySelector(

            ".top-navbar, .top-nav"

        );

        if (!navbar) return;

        if (window.scrollY > 50) {

            navbar.classList.add(

                "navbar-scrolled"

            );

        }

        else {

            navbar.classList.remove(

                "navbar-scrolled"

            );

        }

    }

);


// =========================================================
// COUNTER ANIMATION
// =========================================================

function animateCounter(element) {

    const target = parseInt(

        element.innerText

            .replace("%", "")

            .replace("+", "")

    );

    if (isNaN(target)) return;

    let current = 0;

    const increment =

        target / 60;

    const timer = setInterval(() => {

        current += increment;

        if (current >= target) {

            current = target;

            clearInterval(timer);

        }

        if (element.innerText.includes("%")) {

            element.innerText =

                `${Math.floor(current)}%`;

        }

        else {

            element.innerText =

                Math.floor(current);

        }

    }, 20);

}


// =========================================================
// START COUNTER
// =========================================================

window.addEventListener(

    "load",

    () => {

        const counters =

            document.querySelectorAll(

                ".stats-content h2, .confidence-inner h2, .stat-card h3"

            );

        counters.forEach(counter => {

            animateCounter(counter);

        });

    }

);


// =========================================================
// SCROLL REVEAL
// =========================================================

function revealOnScroll() {

    const reveals = document.querySelectorAll(

        ".stats-card, .analytics-card, .bot-card, .advanced-card, .prediction-card, .info-card"

    );

    reveals.forEach(item => {

        const windowHeight =

            window.innerHeight;

        const revealTop =

            item.getBoundingClientRect().top;

        const revealPoint = 120;

        if (revealTop <

            windowHeight - revealPoint) {

            item.classList.add(

                "active-reveal"

            );

        }

    });

}

window.addEventListener(

    "scroll",

    revealOnScroll

);

revealOnScroll();


// =========================================================
// RANDOM GLOW EFFECT
// =========================================================

function randomGlow() {

    const glowing = document.querySelectorAll(

        ".robot-circle,.confidence-circle"

    );

    glowing.forEach(item => {

        setInterval(() => {

            item.classList.toggle(

                "random-glow"

            );

        }, 2500);

    });

}

randomGlow();


// =========================================================
// AI BOOT EFFECT
// =========================================================

window.addEventListener(

    "load",

    () => {

        const bootMessage = `

=================================================
🌱 ONIONBOT AI PLATFORM
=================================================

🚀 Initializing AI Engine...
🧠 Loading Semantic Search...
📚 Connecting Knowledge Base...
🌐 Internet Search Online...
🤖 Smart Recommendation Ready...

=================================================
SYSTEM READY
=================================================

        `;

        console.log(bootMessage);

    }

);


// =========================================================
// MOUSE GLOW EFFECT
// =========================================================

document.addEventListener(

    "mousemove",

    (e) => {

        let glow = document.querySelector(

            ".cursor-glow"

        );

        if (!glow) {

            glow = document.createElement(

                "div"

            );

            glow.classList.add(

                "cursor-glow"

            );

            document.body.appendChild(

                glow

            );

        }

        glow.style.left =

            `${e.clientX}px`;

        glow.style.top =

            `${e.clientY}px`;

    }

);


// =========================================================
// AUTO CHAT GLOW
// =========================================================

setInterval(() => {

    const chatBox = document.querySelector(

        ".chat-box"

    );

    if (!chatBox) return;

    chatBox.classList.toggle(

        "chat-glow"

    );

}, 3000);


// =========================================================
// BACKGROUND PARALLAX
// =========================================================

window.addEventListener(

    "mousemove",

    (e) => {

        const circles = document.querySelectorAll(

            ".bg-circle"

        );

        circles.forEach((circle, index) => {

            const speed =

                (index + 1) * 0.01;

            const x =

                (window.innerWidth / 2 - e.pageX)

                * speed;

            const y =

                (window.innerHeight / 2 - e.pageY)

                * speed;

            circle.style.transform =

                `translate(${x}px, ${y}px)`;

        });

    }

);


// =========================================================
// MOBILE MENU ANIMATION
// =========================================================

function mobileMenuEffect() {

    const navLinks = document.querySelectorAll(

        ".nav-links a"

    );

    navLinks.forEach(link => {

        link.addEventListener(

            "mouseenter",

            () => {

                link.style.transform =

                    "translateY(-2px)";

            }

        );

        link.addEventListener(

            "mouseleave",

            () => {

                link.style.transform =

                    "translateY(0px)";

            }

        );

    });

}

mobileMenuEffect();


// =========================================================
// AI HEARTBEAT
// =========================================================

setInterval(() => {

    const robotIcon = document.querySelector(

        ".robot-icon"

    );

    if (!robotIcon) return;

    robotIcon.animate(

        [

            {

                transform: "scale(1)"

            },

            {

                transform: "scale(1.08)"

            },

            {

                transform: "scale(1)"

            }

        ],

        {

            duration: 1200

        }

    );

}, 2200);


// =========================================================
// END SYSTEM
// =========================================================

console.log(

    "🚀 OnionBot Animation Engine Active"

);