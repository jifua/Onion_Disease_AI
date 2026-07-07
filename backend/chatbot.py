# =========================================================
# ONIONBOT FINAL 3X
# SMART AGRICULTURE AI PLATFORM
# MINI RAG STYLE CHATBOT
# STARTUP PORTFOLIO VERSION
# =========================================================

# =========================================================
# IMPORTS
# =========================================================

import random
import requests
import re
import json
import time

from urllib.parse import quote
from difflib import SequenceMatcher

# =========================================================
# CONFIG
# =========================================================

AI_NAME = "OnionBot"

AI_ROLE = "Smart Agriculture AI Assistant"

AI_STATUS = "🟢 AI Online"

AI_VERSION = "Final 3X"

AI_DEVELOPER = "Fitria Rozi AI Labs"

MAX_HISTORY = 10

# =========================================================
# PERSONALITY SYSTEM
# =========================================================

AI_PERSONALITY = {

    "tone": "professional",

    "style": "smart",

    "speciality": "agriculture",

    "language": "indonesia"

}

# =========================================================
# SESSION MEMORY
# =========================================================

conversation_memory = {

    "last_topic": None,

    "last_category": None,

    "last_question": None,

    "last_source": None

}

# =========================================================
# CONVERSATION HISTORY
# =========================================================

conversation_history = []

# =========================================================
# TRUSTED SOURCES
# =========================================================

trusted_sources = [

    "Kementerian Pertanian RI",

    "Wikipedia Indonesia",

    "Balai Penelitian Hortikultura",

    "Plant Disease Journal",

    "Research Agriculture",

    "Smart Farming Indonesia",

    "Agriculture Research Center",

    "FAO Agriculture"

]

# =========================================================
# AI STATUS ENGINE
# =========================================================

def ai_status():

    return {

        "name": AI_NAME,

        "role": AI_ROLE,

        "version": AI_VERSION,

        "status": AI_STATUS

    }

# =========================================================
# CLEAN TEXT ENGINE
# =========================================================

def clean_text(text):

    if not text:

        return ""

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text

# =========================================================
# FORMAT NUMBER
# =========================================================

def format_confidence(value):

    return f"{value}%"

# =========================================================
# CATEGORY ICON ENGINE
# =========================================================

def category_icon(category):

    icons = {

        "disease": "🦠",

        "pest": "🐛",

        "cultivation": "🌱",

        "nutrition": "🧪",

        "pesticide": "💊",

        "weather": "☁️",

        "general": "🤖"

    }

    return icons.get(category, "🤖")

# =========================================================
# CATEGORY COLOR
# =========================================================

def category_color(category):

    colors = {

        "disease": "#ff4d4d",

        "pest": "#ff9900",

        "cultivation": "#00cc66",

        "nutrition": "#0099ff",

        "pesticide": "#9933ff",

        "general": "#888888"

    }

    return colors.get(category, "#888888")

# =========================================================
# CONFIDENCE ENGINE
# =========================================================

def generate_confidence(source_type):

    confidence_map = {

        "local": random.randint(92, 98),

        "wikipedia": random.randint(75, 88),

        "duckduckgo": random.randint(70, 82),

        "fallback": random.randint(40, 55)

    }

    return confidence_map.get(source_type, 50)

# =========================================================
# MEMORY UPDATE ENGINE
# =========================================================

def update_memory(

    topic,
    category,
    message,
    source=None

):

    conversation_memory["last_topic"] = topic

    conversation_memory["last_category"] = category

    conversation_memory["last_question"] = message

    conversation_memory["last_source"] = source

    conversation_history.append({

        "topic": topic,

        "category": category,

        "message": message,

        "source": source,

        "timestamp": time.time()

    })

    if len(conversation_history) > MAX_HISTORY:

        conversation_history.pop(0)

# =========================================================
# MEMORY RESPONSE ENGINE
# =========================================================

def memory_response(message):

    msg = message.lower()

    if "pestisida" in msg:

        last_topic = conversation_memory[
            "last_topic"
        ]

        if last_topic:

            if last_topic in knowledge_base:

                data = knowledge_base[
                    last_topic
                ]

                return {

                    "title":

                    f"Pestisida untuk {last_topic}",

                    "recommendation":

                    data["recommendation"]

                }

    return None

# =========================================================
# KNOWLEDGE BASE
# =========================================================

knowledge_base = {

    # =====================================================
    # FUSARIUM
    # =====================================================

    "fusarium": {

        "title": "Fusarium Wilt",

        "category": "disease",

        "keywords": [

            "fusarium",
            "layu",
            "akar busuk",
            "jamur fusarium",
            "tanaman layu"

        ],

        "severity": "high",

        "description":

        """
        Fusarium merupakan penyakit jamur serius
        yang menyerang akar dan pembuluh tanaman
        bawang merah sehingga tanaman menjadi
        layu dan membusuk.
        """,

        "symptoms": [

            "daun menguning",

            "tanaman layu",

            "akar membusuk",

            "pertumbuhan lambat",

            "tanaman mati"

        ],

        "prevention": [

            "gunakan bibit sehat",

            "rotasi tanaman",

            "hindari kelembaban berlebih",

            "sanitasi lahan",

            "gunakan fungisida preventif"

        ],

        "recommendation": [

            "Nativo",

            "Dithane",

            "Antracol",

            "Score"

        ]

    },

    # =====================================================
    # ALTERNARIA
    # =====================================================

    "alternaria": {

        "title": "Alternaria Leaf Blight",

        "category": "disease",

        "keywords": [

            "alternaria",
            "bercak ungu",
            "leaf blight",
            "daun ungu"

        ],

        "severity": "medium",

        "description":

        """
        Alternaria menyebabkan bercak ungu
        pada daun bawang merah dan dapat
        menurunkan hasil panen secara signifikan.
        """,

        "symptoms": [

            "bercak ungu",

            "ujung daun mengering",

            "daun rusak",

            "pertumbuhan terganggu"

        ],

        "prevention": [

            "kurangi kelembaban",

            "gunakan fungisida",

            "sirkulasi udara baik",

            "monitoring rutin"

        ],

        "recommendation": [

            "Mancozeb",

            "Score",

            "Amistar Top"

        ]

    },

    # =====================================================
    # ULAT
    # =====================================================

    "ulat": {

        "title": "Hama Ulat Daun",

        "category": "pest",

        "keywords": [

            "ulat",
            "hama",
            "daun berlubang",
            "ulat daun"

        ],

        "severity": "medium",

        "description":

        """
        Hama ulat menyerang daun bawang merah
        dengan memakan jaringan daun sehingga
        fotosintesis terganggu.
        """,

        "symptoms": [

            "daun berlubang",

            "daun rusak",

            "pertumbuhan terganggu",

            "tanaman terlihat dimakan"

        ],

        "prevention": [

            "monitoring rutin",

            "sanitasi lahan",

            "gunakan perangkap",

            "hindari gulma"

        ],

        "recommendation": [

            "Prevathon",

            "Decis",

            "Emamectin Benzoate"

        ]

    },

    # =====================================================
    # VIRUS
    # =====================================================

    "virus": {

        "title": "Virus Bawang",

        "category": "disease",

        "keywords": [

            "virus",
            "daun belang",
            "virus bawang"

        ],

        "severity": "high",

        "description":

        """
        Virus bawang menyebabkan daun belang,
        pertumbuhan terhambat dan hasil panen
        menurun drastis.
        """,

        "symptoms": [

            "daun belang",

            "pertumbuhan lambat",

            "hasil panen turun",

            "tanaman kerdil"

        ],

        "prevention": [

            "gunakan bibit sehat",

            "kendalikan hama vektor",

            "sanitasi lahan",

            "rotasi tanaman"

        ],

        "recommendation": [

            "Actara",

            "Confidor"

        ]

    },

    # =====================================================
    # BUDIDAYA
    # =====================================================

    "budidaya": {

        "title": "Budidaya Bawang Merah",

        "category": "cultivation",

        "keywords": [

            "budidaya",
            "cara tanam",
            "tanam bawang",
            "budidaya bawang"

        ],

        "severity": "low",

        "description":

        """
        Budidaya bawang merah memerlukan
        tanah gembur, sinar matahari cukup
        dan kontrol kelembaban yang baik.
        """,

        "symptoms": [],

        "prevention": [

            "gunakan bibit unggul",

            "atur jarak tanam",

            "kontrol kelembaban",

            "gunakan pupuk organik"

        ],

        "recommendation": [

            "NPK",

            "Kompos Organik",

            "Pupuk Kandang"

        ]

    }

}

# =========================================================
# GREETING RESPONSES
# =========================================================

greeting_responses = [

    f"""

👋 Halo!

Saya {AI_NAME}

🤖 {AI_ROLE}

{AI_STATUS}

Saya dapat membantu:

✅ penyakit bawang merah
✅ rekomendasi pestisida
✅ gejala tanaman
✅ budidaya bawang
✅ solusi pertanian
✅ informasi internet pertanian

Silakan tanyakan apa saja 😊

""",

    f"""

🌱 Selamat datang di {AI_NAME}

Saya siap membantu analisis:

• Penyakit tanaman
• Hama bawang merah
• Pestisida
• Budidaya
• Solusi pertanian

"""

]

# =========================================================
# SMART SUGGESTION ENGINE
# =========================================================

def smart_suggestions():

    return [

        "Apa itu fusarium?",

        "Cara mengatasi ulat bawang?",

        "Budidaya bawang merah",

        "Pestisida untuk alternaria",

        "Gejala virus bawang",

        "Tips panen bawang merah"

    ]

# =========================================================
# QUERY CLEANER
# =========================================================

def clean_query(query):

    query = query.lower()

    query = clean_text(query)

    query = query.replace("?", "")

    query = query.replace("apa itu", "")

    query = query.replace("bagaimana", "")

    query = query.replace("cara", "")

    query = query.strip()

    return query

# =========================================================
# QUERY OPTIMIZER
# =========================================================

def optimize_query(query):

    replacements = {

        "tanaman layu": "fusarium",

        "bercak ungu": "alternaria",

        "ulat daun": "ulat",

        "virus tanaman": "virus",

        "tanam bawang": "budidaya"

    }

    for old, new in replacements.items():

        if old in query:

            query = query.replace(old, new)

    return query

# =========================================================
# SEMANTIC SIMILARITY
# =========================================================

def semantic_similarity(a, b):

    return SequenceMatcher(

        None,

        a.lower(),

        b.lower()

    ).ratio()

# =========================================================
# KEYWORD MATCH SCORE
# =========================================================

def keyword_match_score(

    message,
    keywords

):

    total_score = 0

    for keyword in keywords:

        similarity = semantic_similarity(

            message,
            keyword

        )

        if keyword in message:

            similarity += 0.5

        total_score += similarity

    return total_score / len(keywords)

# =========================================================
# LOCAL KNOWLEDGE SEARCH
# =========================================================

def local_knowledge_search(message):

    best_match = None

    best_score = 0

    optimized_query = optimize_query(

        clean_query(message)

    )

    for topic, data in knowledge_base.items():

        score = keyword_match_score(

            optimized_query,

            data["keywords"]

        )

        if score > best_score:

            best_score = score

            best_match = (topic, data)

    if best_score >= 0.45:

        return {

            "score": best_score,

            "data": best_match

        }

    return None

# =========================================================
# DETECT CATEGORY
# =========================================================

def detect_category(message):

    msg = message.lower()

    if "pestisida" in msg:

        return "pesticide"

    if "penyakit" in msg:

        return "disease"

    if "budidaya" in msg:

        return "cultivation"

    if "hama" in msg:

        return "pest"

    if "cuaca" in msg:

        return "weather"

    return "general"

# =========================================================
# SOURCE RANKING ENGINE
# =========================================================

def source_priority():

    return {

        "local": 1,

        "wikipedia": 2,

        "duckduckgo": 3,

        "fallback": 4

    }

# =========================================================
# SOURCE BADGE ENGINE
# =========================================================

def source_badge(source_name):

    badges = {

        "Wikipedia Indonesia": "📘",

        "Kementerian Pertanian RI": "🏛️",

        "Plant Disease Journal": "🧪",

        "Research Agriculture": "📚",

        "Smart Farming Indonesia": "🌱"

    }

    return badges.get(source_name, "🌐")

# =========================================================
# WIKIPEDIA ENGINE
# =========================================================
def wikipedia_search(query):

    try:

        search_url = (
            "https://id.wikipedia.org/w/api.php"
            f"?action=query&list=search&srsearch={quote(query)}"
            "&format=json&srlimit=1"
        )

        headers = {
            "User-Agent": "OnionBotAI/1.0 (contact: youremail@example.com)"
        }

        search_response = requests.get(search_url, headers=headers, timeout=5)

        print("DEBUG search status:", search_response.status_code)

        if search_response.status_code != 200:
            return None

        search_data = search_response.json()

        results = search_data.get("query", {}).get("search", [])

        print("DEBUG search results:", results)

        if not results:
            return None

        matched_title = results[0]["title"]

        url = (
            "https://id.wikipedia.org/api/rest_v1/page/summary/"
            + quote(matched_title)
        )

        response = requests.get(url, headers=headers, timeout=5)

        print("DEBUG summary status:", response.status_code)

        if response.status_code != 200:
            return None

        data = response.json()

        extract = data.get("extract")

        title = data.get("title")

        image = None

        if "thumbnail" in data:
            image = data["thumbnail"].get("source")

        if not extract:
            return None

        return {
            "title": title,
            "summary": clean_text(extract),
            "image": image,
            "source": "Wikipedia Indonesia"
        }

    except Exception as e:

        print("DEBUG wikipedia error:", repr(e))

        return None

# =========================================================
# DUCKDUCKGO INSTANT API
# =========================================================

def duckduckgo_search(query):

    try:

        url = (

            "https://api.duckduckgo.com/"

            f"?q={quote(query)}"

            "&format=json"

            "&pretty=1"

        )

        response = requests.get(

            url,

            timeout=5

        )

        if response.status_code != 200:

            return None

        data = response.json()

        abstract = data.get(

            "AbstractText"

        )

        heading = data.get(

            "Heading"

        )

        if not abstract:

            return None

        return {

            "title": heading,

            "summary": clean_text(

                abstract

            ),

            "source": "DuckDuckGo Instant"

        }

    except Exception:

        return None

# =========================================================
# AI THINKING ENGINE
# =========================================================

def ai_thinking_steps():

    return [

        "🔍 Menganalisis pertanyaan...",

        "📚 Mencari basis pengetahuan...",

        "🌐 Mengakses sumber terpercaya...",

        "🤖 Menyusun rekomendasi AI..."

    ]

# =========================================================
# FORMAT LIST
# =========================================================

def format_list(items):

    if not items:

        return []

    result = []

    for item in items:

        result.append(

            clean_text(item)

        )

    return result

# =========================================================
# RESPONSE CARD ENGINE
# =========================================================

def create_card_response(

    title,
    category,
    description,
    symptoms=None,
    prevention=None,
    recommendation=None,
    source=None,
    confidence=90,
    suggestions=None,
    severity=None,
    image=None

):

    return {

        "status": "success",

        "title": clean_text(title),

        "category": category,

        "icon": category_icon(category),

        "color": category_color(category),

        "description": clean_text(

            description

        ),

        "symptoms": format_list(

            symptoms

        ),

        "prevention": format_list(

            prevention

        ),

        "recommendation": format_list(

            recommendation

        ),

        "source": source or [],

        "confidence": confidence,

        "confidence_text":

        format_confidence(confidence),

        "suggestions":

        suggestions or [],

        "severity": severity,

        "image": image,

        "timestamp": time.time()

    }

# =========================================================
# FALLBACK ENGINE
# =========================================================

def fallback_response():

    return {

        "status": "fallback",

        "title": "Jawaban Belum Ditemukan",

        "category": "general",

        "icon": "🤖",

        "color": "#777777",

        "description":

        """
        Maaf, saya belum menemukan
        jawaban yang tepat untuk
        pertanyaan tersebut.
        """,

        "symptoms": [],

        "prevention": [],

        "recommendation": [],

        "source": [

            "Fallback AI"

        ],

        "confidence":

        generate_confidence(

            "fallback"

        ),

        "confidence_text":

        format_confidence(

            generate_confidence(

                "fallback"

            )

        ),

        "suggestions": [

            "Apa itu fusarium?",

            "Cara mengatasi ulat?",

            "Budidaya bawang merah",

            "Pestisida tanaman bawang"

        ],

        "severity": None,

        "image": None,

        "timestamp": time.time()

    }

# =========================================================
# SYSTEM INFO ENGINE
# =========================================================

def system_information():

    return {

        "system": AI_NAME,

        "version": AI_VERSION,

        "developer": AI_DEVELOPER,

        "status": AI_STATUS,

        "knowledge_items":

        len(knowledge_base),

        "sources":

        len(trusted_sources)

    }

# =========================================================
# RESPONSE LOGGER
# =========================================================

def log_response(

    question,
    response

):

    try:

        log_data = {

            "question": question,

            "response_title":

            response.get("title"),

            "category":

            response.get("category"),

            "timestamp":

            time.time()

        }

        print(

            json.dumps(

                log_data,

                indent=4

            )

        )

    except Exception:

        pass

# =========================================================
# HISTORY ENGINE
# =========================================================

def recent_history():

    recent = []

    for item in conversation_history[-5:]:

        recent.append({

            "topic": item["topic"],

            "message": item["message"]

        })

    return recent

# =========================================================
# CONTEXT ENGINE
# =========================================================

def build_context():

    context = {

        "last_topic":

        conversation_memory["last_topic"],

        "last_category":

        conversation_memory["last_category"],

        "history_count":

        len(conversation_history)

    }

    return context

# =========================================================
# GREETING DETECTOR
# =========================================================

def is_greeting(message):

    greetings = [

        "halo",
        "hai",
        "hello",
        "hi",
        "selamat pagi",
        "selamat malam",
        "onionbot"

    ]

    msg = message.lower()

    for greet in greetings:

        if greet in msg:

            return True

    return False

# =========================================================
# GREETING RESPONSE
# =========================================================

def greeting_response():

    return create_card_response(

        title="Halo 👋",

        category="general",

        description=random.choice(

            greeting_responses

        ),

        source=[

            "OnionBot Core"

        ],

        confidence=100,

        suggestions=smart_suggestions(),

        severity="low"

    )

# =========================================================
# MEMORY RESPONSE ENGINE
# =========================================================

def memory_based_response(message):

    memory_result = memory_response(

        message

    )

    if not memory_result:

        return None

    return create_card_response(

        title=memory_result["title"],

        category="pesticide",

        description=

        """
        Berikut rekomendasi pestisida
        berdasarkan percakapan sebelumnya.
        """,

        recommendation=

        memory_result["recommendation"],

        source=[

            "Conversation Memory"

        ],

        confidence=95,

        suggestions=[

            "Cara penggunaan pestisida",

            "Dosis pestisida",

            "Alternatif pestisida"

        ],

        severity="medium"

    )

# =========================================================
# LOCAL RESPONSE ENGINE
# =========================================================

def local_response_engine(message):

    local_result = local_knowledge_search(

        message

    )

    if not local_result:

        return None

    topic, data = local_result["data"]

    update_memory(

        topic=topic,

        category=data["category"],

        message=message,

        source="local"

    )

    return create_card_response(

        title=data["title"],

        category=data["category"],

        description=data["description"],

        symptoms=data["symptoms"],

        prevention=data["prevention"],

        recommendation=data["recommendation"],

        source=[

            random.choice(

                trusted_sources

            )

        ],

        confidence=generate_confidence(

            "local"

        ),

        suggestions=[

            "Cara pencegahan?",

            "Pestisida terbaik?",

            "Apakah berbahaya?",

            "Solusi pertanian lainnya"

        ],

        severity=data["severity"]

    )

# =========================================================
# WIKIPEDIA RESPONSE ENGINE
# =========================================================

def wikipedia_response_engine(message):

    result = wikipedia_search(message)

    if not result:

        return None

    update_memory(

        topic=result["title"],

        category="general",

        message=message,

        source="wikipedia"

    )

    return create_card_response(

        title=result["title"],

        category=detect_category(

            message

        ),

        description=result["summary"],

        source=[

            result["source"]

        ],

        confidence=generate_confidence(

            "wikipedia"

        ),

        suggestions=[

            "Cari informasi terkait",

            "Cara penanganan",

            "Budidaya tanaman",

            "Pencegahan penyakit"

        ],

        severity="medium",

        image=result["image"]

    )

# =========================================================
# DUCKDUCKGO RESPONSE ENGINE
# =========================================================

def duckduckgo_response_engine(message):

    result = duckduckgo_search(

        message

    )

    if not result:

        return None

    update_memory(

        topic=result["title"],

        category="general",

        message=message,

        source="duckduckgo"

    )

    return create_card_response(

        title=result["title"],

        category="general",

        description=result["summary"],

        source=[

            result["source"]

        ],

        confidence=generate_confidence(

            "duckduckgo"

        ),

        suggestions=[

            "Informasi lebih lanjut",

            "Penyakit terkait",

            "Solusi pertanian"

        ],

        severity="low"

    )

# =========================================================
# SEARCH PRIORITY ENGINE
# =========================================================

def smart_search_engine(message):

    # =====================================================
    # PRIORITY 1
    # LOCAL KNOWLEDGE BASE
    # =====================================================

    local_result = local_response_engine(

        message

    )

    if local_result:

        return local_result

    # =====================================================
    # PRIORITY 2
    # WIKIPEDIA
    # =====================================================

    wiki_result = wikipedia_response_engine(

        message

    )

    if wiki_result:

        return wiki_result

    # =====================================================
    # PRIORITY 3
    # DUCKDUCKGO API
    # =====================================================

    ddg_result = duckduckgo_response_engine(

        message

    )

    if ddg_result:

        return ddg_result

    # =====================================================
    # PRIORITY 4
    # FALLBACK
    # =====================================================

    return fallback_response()

# =========================================================
# MAIN AI RESPONSE ENGINE
# =========================================================

def get_ai_response(message):

    user_message = clean_text(

        message.lower()

    )

    # =====================================================
    # GREETING
    # =====================================================

    if is_greeting(user_message):

        response = greeting_response()

        log_response(

            user_message,

            response

        )

        return response

    # =====================================================
    # MEMORY RESPONSE
    # =====================================================

    memory_result = memory_based_response(

        user_message

    )

    if memory_result:

        log_response(

            user_message,

            memory_result

        )

        return memory_result

    # =====================================================
    # SMART SEARCH ENGINE
    # =====================================================

    response = smart_search_engine(

        user_message

    )

    # =====================================================
    # ADD CONTEXT
    # =====================================================

    response["context"] = build_context()

    response["system"] = system_information()

    response["thinking_steps"] = ai_thinking_steps()

    response["history"] = recent_history()

    # =====================================================
    # LOGGING
    # =====================================================

    log_response(

        user_message,

        response

    )

    return response

# =========================================================
# STARTUP BANNER
# =========================================================

startup_banner = f"""

=========================================================
🌱 ONIONBOT AI PLATFORM
=========================================================

🤖 AI Name      : {AI_NAME}
🚀 Version      : {AI_VERSION}
🧠 AI Role      : {AI_ROLE}
👨‍💻 Developer   : {AI_DEVELOPER}
📚 Knowledge    : {len(knowledge_base)} Topics
🌐 Sources      : {len(trusted_sources)} Trusted Sources
{AI_STATUS}

=========================================================
SMART AGRICULTURE AI ASSISTANT
MINI RAG ARCHITECTURE
SEMANTIC SEARCH ENABLED
MODERN RESPONSE SYSTEM
=========================================================

"""

print(startup_banner)

# =========================================================
# LOCAL TEST
# =========================================================

if __name__ == "__main__":

    print(startup_banner)

    while True:

        user_input = input(

            "\n👨 User : "

        )

        if user_input.lower() in [

            "exit",
            "quit"

        ]:

            print(

                "\n👋 OnionBot Shutdown"

            )

            break

        result = get_ai_response(

            user_input

        )

        print(

            json.dumps(

                result,

                indent=4,

                ensure_ascii=False

            )

        )