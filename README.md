# Vue 3 + TypeScript + Vite

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about the recommended Project Setup and IDE Support in the [Vue Docs TypeScript Guide](https://vuejs.org/guide/typescript/overview.html#project-setup).

Todo:
upload backend to server hosting (e.g. render)
reconnect api server to frontend


Documentation:

npm run dev
npm run build

git add .
git commit -m "message"
git push origin main

color theme:
#666
#111
#f8f9fa
#b9c9d8
#bed8b9
#FAF9F6

windows
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn google-genai python-dotenv

pip install -r requirements.txt
pip freeze > requirements.txt

mac
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn google-genai python-dotenv
pip freeze > requirements.txt

uvicorn app.main:app --reload
uvicorn app.main:app --host 0.0.0.0 --port 10000
