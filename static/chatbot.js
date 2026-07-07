// =========================================================
// ONIONBOT AI PLATFORM
// CHATBOT ENGINE FINAL 3X
// =========================================================


// =========================================================
// ELEMENTS
// =========================================================

const form = document.getElementById(
    "chat-form"
);

const input = document.getElementById(
    "user-input"
);

const chatBox = document.getElementById(
    "chat-box"
);


// =========================================================
// LOADING MESSAGES
// =========================================================

const loadingMessages = [

    "🔍 Menganalisis pertanyaan...",

    "📚 Mencari knowledge base...",

    "🌐 Mengakses sumber AI...",

    "🤖 Menyusun jawaban AI...",

    "🧠 Menjalankan semantic search...",

    "🌱 Menyiapkan solusi pertanian..."

];


// =========================================================
// RANDOM LOADING MESSAGE
// =========================================================

function randomLoadingMessage() {

    return loadingMessages[

        Math.floor(

            Math.random()

            * loadingMessages.length

        )

    ];

}


// =========================================================
// AUTO SCROLL
// =========================================================

function autoScroll() {

    chatBox.scrollTop =

        chatBox.scrollHeight;

}


// =========================================================
// QUICK QUESTION
// =========================================================

function askQuickQuestion(question) {

    input.value = question;

    form.dispatchEvent(

        new Event("submit")

    );

}


// =========================================================
// CONFIDENCE COLOR
// =========================================================

function confidenceColor(value) {

    if (value >= 90) {

        return "#00f5a0";

    }

    if (value >= 75) {

        return "#ffcc00";

    }

    return "#ff4d4d";

}


// =========================================================
// RENDER THINKING STEP
// =========================================================

function renderThinkingSteps(steps) {

    if (!steps || steps.length === 0) {

        return "";

    }

    return `

        <div class="thinking-container">

            ${steps.map(step => `

                <div class="thinking-step">

                    ${step}

                </div>

            `).join("")}

        </div>

    `;

}


// =========================================================
// RENDER LIST
// =========================================================

function renderList(title, items) {

    if (!items || items.length === 0) {

        return "";

    }

    return `

        <div class="response-section">

            <h3>

                ${title}

            </h3>

            <ul>

                ${items.map(item => `

                    <li>

                        ${item}

                    </li>

                `).join("")}

            </ul>

        </div>

    `;

}


// =========================================================
// RENDER SOURCES
// =========================================================

function renderSources(sources) {

    if (!sources || sources.length === 0) {

        return "";

    }

    return `

        <div class="source-container">

            ${sources.map(source => `

                <div class="source-badge">

                    🌐 ${source}

                </div>

            `).join("")}

        </div>

    `;

}


// =========================================================
// RENDER IMAGE
// =========================================================

function renderImage(image) {

    if (!image) {

        return "";

    }

    return `

        <div class="response-image-container">

            <img src="${image}"

                 class="response-image">

        </div>

    `;

}


// =========================================================
// RENDER CONFIDENCE
// =========================================================

function renderConfidence(confidence) {

    return `

        <div class="confidence-wrapper">

            <div class="confidence-text">

                AI Confidence

            </div>

            <div class="confidence-bar">

                <div class="confidence-fill"

                     style="

                     width:${confidence}%;

                     background:${confidenceColor(confidence)}

                     ">

                </div>

            </div>

            <div class="confidence-value">

                ${confidence}%

            </div>

        </div>

    `;

}


// =========================================================
// RENDER CATEGORY
// =========================================================

function renderCategory(category, icon) {

    return `

        <div class="category-badge">

            ${icon}

            ${category}

        </div>

    `;

}


// =========================================================
// RENDER SUGGESTION
// =========================================================

function renderSuggestions(suggestions) {

    if (!suggestions ||
        suggestions.length === 0) {

        return "";

    }

    return `

        <div class="suggestion-container">

            ${suggestions.map(

                suggestion => `

                <button

                    class="suggestion-chip"

                    onclick="askQuickQuestion('${suggestion}')"

                >

                    ${suggestion}

                </button>

            `).join("")}

        </div>

    `;

}


// =========================================================
// USER MESSAGE
// =========================================================

function renderUserMessage(message) {

    return `

        <div class="user-message">

            ${message}

        </div>

    `;

}


// =========================================================
// TYPING MESSAGE
// =========================================================

function renderTypingMessage() {

    return `

        <div class="typing-container"
             id="typing">

            <div class="typing-header">

                🤖 OnionBot AI

            </div>

            <div class="typing-animation">

                <span></span>

                <span></span>

                <span></span>

            </div>

            <div class="typing-text">

                ${randomLoadingMessage()}

            </div>

        </div>

    `;

}


// =========================================================
// ERROR CARD
// =========================================================

function renderErrorCard() {

    return `

        <div class="error-card">

            <div class="error-icon">

                ⚠️

            </div>

            <div>

                AI Engine gagal terhubung.

            </div>

        </div>

    `;

}


// =========================================================
// BOT CARD ENGINE
// =========================================================

function renderBotCard(data) {

    return `

    <div class="bot-card">

        <!-- TOP -->

        <div class="bot-card-top">

            ${renderCategory(

                data.category,

                data.icon

            )}

            ${renderConfidence(

                data.confidence

            )}

        </div>

        <!-- TITLE -->

        <div class="bot-card-title">

            ${data.title}

        </div>

        <!-- IMAGE -->

        ${renderImage(
            data.image
        )}

        <!-- DESCRIPTION -->

        <div class="bot-description">

            ${data.description}

        </div>

        <!-- SYMPTOMS -->

        ${renderList(
            "⚠️ Gejala",
            data.symptoms
        )}

        <!-- PREVENTION -->

        ${renderList(
            "🛡️ Pencegahan",
            data.prevention
        )}

        <!-- RECOMMENDATION -->

        ${renderList(
            "💊 Rekomendasi",
            data.recommendation
        )}

        <!-- SOURCE -->

        ${renderSources(
            data.source
        )}

        <!-- SUGGESTIONS -->

        ${renderSuggestions(
            data.suggestions
        )}

    </div>

    `;

}


// =========================================================
// UPDATE TYPING TEXT
// =========================================================

function updateTypingText() {

    const typingText =

        document.querySelector(
            ".typing-text"
        );

    if (typingText) {

        typingText.innerHTML =

            randomLoadingMessage();

    }

}


// =========================================================
// SEND MESSAGE
// =========================================================

form.addEventListener(

    "submit",

    async (e) => {

        e.preventDefault();

        const userMessage =

            input.value.trim();

        if (!userMessage) return;

        // USER MESSAGE

        chatBox.innerHTML +=

            renderUserMessage(
                userMessage
            );

        // RESET INPUT

        input.value = "";

        // TYPING

        chatBox.innerHTML +=

            renderTypingMessage();

        autoScroll();

        // LOADING ANIMATION

        const typingInterval =

            setInterval(

                updateTypingText,

                1500

            );

        try {

            // API CALL

            const response = await fetch(

                "/chatbot-api",

                {

                    method: "POST",

                    headers: {

                        "Content-Type":

                        "application/json"

                    },

                    body: JSON.stringify({

                        message: userMessage

                    })

                }

            );

            // JSON

            const data =

                await response.json();

            // REMOVE TYPING

            clearInterval(

                typingInterval

            );

            document.getElementById(
                "typing"
            ).remove();

            // BOT CARD

            chatBox.innerHTML +=

                renderBotCard(data);

            autoScroll();

        }

        catch (error) {

            clearInterval(
                typingInterval
            );

            document.getElementById(
                "typing"
            ).remove();

            chatBox.innerHTML +=

                renderErrorCard();

            autoScroll();

            console.error(error);

        }

    }

);


// =========================================================
// ENTER SHORTCUT
// =========================================================

input.addEventListener(

    "keypress",

    function(event) {

        if (event.key === "Enter") {

            form.dispatchEvent(

                new Event("submit")

            );

        }

    }

);


// =========================================================
// AUTO FOCUS
// =========================================================

window.onload = () => {

    input.focus();

};


// =========================================================
// AI SYSTEM INFO
// =========================================================

console.log(`

=================================================
🌱 ONIONBOT AI PLATFORM
=================================================

🤖 Smart Agriculture AI
🚀 Mini RAG Architecture
🧠 Semantic Search Enabled
🌐 AI Knowledge Engine
📚 Agriculture Intelligence

=================================================

`);


// =========================================================
// ONLINE DOT EFFECT
// =========================================================

setInterval(() => {

    const onlineDot =

        document.querySelector(
            ".online-dot"
        );

    if (onlineDot) {

        onlineDot.classList.toggle(
            "online-pulse"
        );

    }

}, 1500);


// =========================================================
// HERO GLOW EFFECT
// =========================================================

setInterval(() => {

    const robotCircle =

        document.querySelector(
            ".robot-circle"
        );

    if (robotCircle) {

        robotCircle.classList.toggle(
            "robot-glow"
        );

    }

}, 3000);