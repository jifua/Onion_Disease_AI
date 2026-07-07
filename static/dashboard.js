// =========================================================
// ONIONBOT AI PLATFORM
// DASHBOARD ENGINE FINAL 3X
// =========================================================


// =========================================================
// SYSTEM STATUS
// =========================================================

const systemStatus = {

    ai: "Online",

    cnn: "Active",

    semantic: "Running",

    database: "Connected",

    internet: "Stable"

};

console.table(systemStatus);


// =========================================================
// LIVE CLOCK
// =========================================================

function updateClock() {

    const clock = document.querySelector(

        ".live-clock"

    );

    if (!clock) return;

    const now = new Date();

    clock.innerHTML =

        now.toLocaleTimeString();

}

setInterval(updateClock, 1000);


// =========================================================
// RANDOM ACTIVITY UPDATE
// =========================================================

const activityMessages = [

    "AI melakukan semantic search",

    "CNN berhasil mendeteksi penyakit",

    "Database prediction diperbarui",

    "AI recommendation engine aktif",

    "Knowledge base diperbarui",

    "Sistem AI berjalan stabil",

    "OnionBot menganalisis data tanaman"

];


// =========================================================
// RANDOM ACTIVITY
// =========================================================

function randomActivity() {

    const activityList = document.querySelector(

        ".activity-list"

    );

    if (!activityList) return;

    const activity = document.createElement(

        "div"

    );

    activity.classList.add(

        "activity-item"

    );

    activity.innerHTML = `

        <div class="activity-dot"></div>

        ${activityMessages[

            Math.floor(

                Math.random()

                * activityMessages.length

            )

        ]}

    `;

    activityList.prepend(activity);

    if (

        activityList.children.length > 6

    ) {

        activityList.removeChild(

            activityList.lastChild

        );

    }

}

setInterval(randomActivity, 6000);


// =========================================================
// COUNTER ANIMATION
// =========================================================

function animateCounter(element) {

    const target = parseInt(

        element.innerText

            .replace("%", "")

            .replace("+", "")

            .replace(",", "")

    );

    if (isNaN(target)) return;

    let current = 0;

    const increment = target / 60;

    const timer = setInterval(() => {

        current += increment;

        if (current >= target) {

            current = target;

            clearInterval(timer);

        }

        if (

            element.innerText.includes("%")

        ) {

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

                ".stats-card h2, .confidence-inner h2, .analytics-card h2"

            );

        counters.forEach(counter => {

            animateCounter(counter);

        });

    }

);


// =========================================================
// CARD HOVER EFFECT
// =========================================================

function cardHoverEffect() {

    const cards = document.querySelectorAll(

        ".stats-card, .analytics-card, .prediction-card, .advanced-card"

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

                    ((y - centerY) / 25);

                const rotateY =

                    ((centerX - x) / 25);

                card.style.transform =

                    `perspective(1000px)
                     rotateX(${rotateX}deg)
                     rotateY(${rotateY}deg)
                     translateY(-6px)`;

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
// SCROLL REVEAL
// =========================================================

function revealOnScroll() {

    const reveals = document.querySelectorAll(

        ".stats-card, .analytics-card, .advanced-card, .prediction-card"

    );

    reveals.forEach(item => {

        const windowHeight =

            window.innerHeight;

        const revealTop =

            item.getBoundingClientRect().top;

        const revealPoint = 120;

        if (

            revealTop <

            windowHeight - revealPoint

        ) {

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
// RANDOM GLOW
// =========================================================

function randomGlow() {

    const glowing = document.querySelectorAll(

        ".confidence-circle, .chart-container"

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
// ONLINE DOT EFFECT
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
// CHART ANIMATION
// =========================================================

function animateChartBars() {

    const bars = document.querySelectorAll(

        ".chart-bar"

    );

    bars.forEach(bar => {

        const height =

            bar.dataset.height;

        bar.style.height = "0px";

        setTimeout(() => {

            bar.style.height =

                `${height}%`;

        }, 500);

    });

}

animateChartBars();


// =========================================================
// AI ENGINE EFFECT
// =========================================================

function aiEngineEffect() {

    const engines = document.querySelectorAll(

        ".engine-status"

    );

    engines.forEach(engine => {

        setInterval(() => {

            engine.classList.toggle(

                "engine-pulse"

            );

        }, 1800);

    });

}

aiEngineEffect();


// =========================================================
// BACKGROUND PARTICLE
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

setInterval(createParticle, 1000);


// =========================================================
// PARALLAX EFFECT
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
// NAVBAR EFFECT
// =========================================================

window.addEventListener(

    "scroll",

    () => {

        const navbar = document.querySelector(

            ".top-navbar"

        );

        if (!navbar) return;

        if (window.scrollY > 40) {

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
// SYSTEM BOOT
// =========================================================

window.addEventListener(

    "load",

    () => {

        console.log(`

=================================================
🌱 ONIONBOT AI DASHBOARD
=================================================

🚀 AI Analytics Active
🧠 Semantic Engine Running
📚 Knowledge Base Connected
🌐 Internet Search Stable
🤖 CNN Detection Ready

=================================================
SYSTEM READY
=================================================

        `);

    }

);


// =========================================================
// AUTO REFRESH INDICATOR
// =========================================================

setInterval(() => {

    const indicators = document.querySelectorAll(

        ".status-indicator"

    );

    indicators.forEach(item => {

        item.classList.toggle(

            "indicator-active"

        );

    });

}, 2000);


// =========================================================
// FLOATING ICON EFFECT
// =========================================================

function floatingEffect() {

    const icons = document.querySelectorAll(

        ".prediction-icon"

    );

    icons.forEach((icon, index) => {

        setInterval(() => {

            icon.animate(

                [

                    {

                        transform: "translateY(0px)"

                    },

                    {

                        transform: "translateY(-6px)"

                    },

                    {

                        transform: "translateY(0px)"

                    }

                ],

                {

                    duration: 1800,

                    delay: index * 200

                }

            );

        }, 2500);

    });

}

floatingEffect();


// =========================================================
// END SYSTEM
// =========================================================

console.log(

    "🚀 Dashboard Engine Active"

);