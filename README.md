# Unblur

Unblur is an AI-powered accessibility reader designed to improve text readability through dynamic typography controls and AI-based text simplification.

Built with Vue 3 + FastAPI + Gemini API.

---

## ✨ Features

- AI-powered text simplification
- Adjustable typography controls
  - Font size
  - Line height
  - Letter spacing
  - Max width
  - Theme (Light / Dark / Sepia)
- Centralized state management (Pinia)
- Responsive layout (Tailwind CSS)

---

## 🛠 Tech Stack

Frontend:
- Vue 3 + TypeScript
- Pinia
- Tailwind CSS
- Vite

Backend:
- FastAPI
- Google Gemini API
- Python 3

Deployment:
- Frontend: Vercel
- Backend: Render

---

## 🏗 Architecture

Frontend → `/optimize` endpoint → FastAPI → Gemini API → simplified text returned → ReaderView updates.

Typography state is centrally managed via Pinia.

---

## 🚀 Local Development

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Create frontend/.env:
VITE_API_URL=http://127.0.0.1:8000

Vercel frontend requires:
VITE_API_URL=https://your-render-url.onrender.com

### Backend

Mac / Linux
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Windows
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Create backend/.env:
GEMINI_API_KEY=your_api_key_here

Render runs backend with:
uvicorn app.main:app --host 0.0.0.0 --port 10000

## 📌 Motivation

Unblur explores accessibility-first UI design and AI-assisted text simplification.
The project focuses on clean state management, full-stack integration, and scalable architecture.

Future improvements will expand adaptive personalization and richer text analysis.
