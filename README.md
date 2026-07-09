# 🧅 OnionBot AI Platform

**AI-powered onion disease detection & smart agriculture assistant** — built end-to-end with a deep learning model, a REST API backend, and a mini-RAG chatbot, deployed to production with Docker.

🔗 **Live Demo:** [huggingface.co/spaces/jifua19/onion-disease-ai](https://huggingface.co/spaces/jifua19/onion-disease-ai)

---

## 📸 Preview

### Home & Disease Detection
![Home page](readme_assets/screenshot-home.png)

### AI Chatbot
![Chatbot page](readme_assets/screenshot-chatbot.png)

---

## 📖 About

OnionBot AI Platform helps shallot (onion) farmers quickly identify leaf diseases from a photo and get actionable treatment recommendations. Beyond image classification, it includes a conversational AI assistant that answers agriculture-related questions using a local knowledge base combined with live Wikipedia search — without relying on a large paid LLM API.

This project was built as a personal, self-directed engineering exercise covering the full stack: model deployment, backend API design, database, chatbot logic, containerization, and cloud deployment.

## ✨ Features

- 🔍 **Disease Detection** — upload a leaf image, get a prediction with confidence score and treatment recommendation
- 💬 **AI Chatbot** — ask natural-language questions about onion diseases, pests, cultivation, and pesticides; falls back to Wikipedia search when the local knowledge base doesn't have an answer
- 📊 **Analytics Dashboard** — track total predictions, average confidence, and most common disease detected
- 🕘 **Prediction History** — every prediction is logged to a local database
- 🔐 **User Authentication** — basic register/login system

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| AI Inference | ONNX Runtime (converted from a TensorFlow/Keras model) |
| Image Processing | OpenCV (headless) |
| Chatbot | Custom mini-RAG: local keyword-matching knowledge base + Wikipedia API fallback |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Deployment | Docker, Hugging Face Spaces |

## 🏗️ Architecture

```
User uploads image
        │
        ▼
   FastAPI Backend
        │
        ▼
  ONNX Runtime Model  ──▶  Prediction + Confidence Score
        │
        ▼
  Knowledge Base Lookup  ──▶  Treatment Recommendation
        │
        ▼
   Save to SQLite  ──▶  History & Dashboard
```

```
User asks a question (Chatbot)
        │
        ▼
  Local Knowledge Base Search (keyword/semantic match)
        │
        ├── Match found  ──▶  Return structured answer
        │
        └── No match  ──▶  Wikipedia Search API  ──▶  Return summarized answer
```

## 🚀 Running Locally

**Prerequisites:** Python 3.9+, pip

```bash
# Clone the repository
git clone https://github.com/jifua/Onion_Disease_AI.git
cd Onion_Disease_AI/onion_disease_ai

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn backend.app:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

## 🐳 Running with Docker

```bash
docker build -t onionbot-ai .
docker run -p 7860:7860 onionbot-ai
```

## 📂 Project Structure

```
onion_disease_ai/
├── backend/
│   ├── app.py              # FastAPI routes & app entrypoint
│   ├── chatbot.py          # Mini-RAG chatbot engine
│   ├── database.py         # SQLite database logic
│   ├── disease_info.py     # Disease knowledge base
│   └── utils.py            # Model loading & prediction logic
├── model/                  # ONNX model file
├── static/                 # CSS, JS, images
├── templates/               # HTML templates (Jinja2)
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🗺️ Roadmap

- [ ] Migrate chatbot retrieval to embedding-based semantic search
- [ ] Add multi-crop support (tomato, rice, corn)
- [ ] Add a mobile-friendly camera capture flow
- [ ] Improve authentication with hashed passwords & JWT

## 👤 Author

**Fitria Rozi**
[LinkedIn](https://www.linkedin.com/in/fitria-rozi-6a344a1b1/) · [GitHub](https://github.com/jifua)

---

*This project was built independently as a hands-on learning exercise in full-stack AI application development.*
