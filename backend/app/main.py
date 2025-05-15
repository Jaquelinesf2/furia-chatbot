from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import google.generativeai as genai
import traceback
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pathlib

# Carregar variáveis do .env
load_dotenv()

# Inicializar FastAPI
app = FastAPI()

# Base directory deste arquivo
BASE_DIR = pathlib.Path(__file__).parent
frontend_dir = BASE_DIR / "frontend"

# Servir arquivos estáticos (JS, CSS, imagens)
app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

# Configurar a API do Google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# (Opcional) Listar modelos que suportam generateContent
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

# Permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de requisição
class ChatRequest(BaseModel):
    pergunta: str

# Rota para carregar o HTML
@app.get("/", response_class=FileResponse)
def read_index():
    return FileResponse(str(frontend_dir / "index.html"))

# Rota de chat com prompt injetado
@app.post("/chat")
async def chat_furia(request: ChatRequest):
    try:
        print("Pergunta recebida:", request.pergunta)  # Debug: exibe a pergunta no terminal

        pergunta = request.pergunta.strip()
        roster = "KSCERATO, arT, FalleN, chelo, yuurih"

        prompt = f"""
Você é o assistente oficial da FURIA CS:GO, um chatbot amigável e bem-humorado.
Responda sempre em português coloquial, focado no universo de CS:GO da FURIA.
A line-up atual de CS:GO da FURIA é: {roster}.
Não peça para o usuário checar outros sites, apenas responda com base nessas informações.

Pergunta: {pergunta}
Resposta:
"""

        model = genai.GenerativeModel("models/gemini-1.5-pro")
        response = model.generate_content(prompt)
        answer = response.text.strip()

        return {"resposta": answer}

    except Exception as e:
        traceback.print_exc()  # Mostra o erro no terminal
        raise HTTPException(status_code=422, detail=str(e))  # Responde com erro 422 e a descrição
