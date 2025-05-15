# 🐱‍👤 Fúria Chatbot - Esportes & Interatividade

Projeto de chatbot interativo para fãs de esportes, desenvolvido com **Python (FastAPI)** e integrado à **Google Gemini API**.

---

## 📋 Descrição
O **Fúria Chatbot** é uma aplicação que responde perguntas sobre o time Fúria (esportes), permitindo interação via API. Utiliza IA generativa para fornecer respostas dinâmicas.

---

## 🚀 Tecnologias Utilizadas
- 🐍 Python 3.x
- ⚡ FastAPI
- 🌐 Uvicorn (servidor ASGI)
- 🧠 Google Gemini API (Generative AI)
- 🗂️ HTML + CSS (Frontend estático simples)
- 🧰 JavaScript (para consumo da API)

---

## 🏗️ Estrutura do Projeto
furia-chatbot/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── schemas.py
│ │ └── ...
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── .gitignore
├── README.md
└── venv/ (ignorado no git)


---

## 🛠️ Como rodar o projeto localmente

### 1. Clone o repositório
```bash
git clone https://github.com/Jaquelinesf2/furia-chatbot.git
cd furia-chatbot

### 2. Crie o ambiente virtual
python -m venv venv

### 3. Ative o ambiente virtual
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate


### 4. Instale as dependências  
pip install -r backend/requirements.txt

### 5. Configure a API KEY da Gemini
Crie um arquivo .env dentro de backend/app/ com:
GEMINI_API_KEY=sua-chave-aqui

### 6. Rode o servidor FastAPI
uvicorn backend.app.main:app --reload

### 7. Acesse no navegador:
http://127.0.0.1:8000/

📝 Observações
O projeto usa a cota gratuita da Gemini API. Limites podem ser atingidos com uso excessivo.

O frontend é estático e consome a API backend.

🤝 Contribuição
Sinta-se à vontade para enviar sugestões, melhorias ou abrir issues!

🐱‍💻 Desenvolvido por
Jaqueline da Silva Freitas
