# 🌌 Nebula Chat

Nebula Chat is a modern AI-powered chatbot application built using Django and deployed on Vercel. It integrates powerful large language models through OpenRouter and provides an interactive cosmic-themed chat experience.

---

## 🚀 Features

- 🤖 AI-powered conversational chatbot
- 🌌 Modern cosmic-themed UI
- ⚡ Fast deployment using Vercel
- 🔐 Secure API key management using environment variables
- 💬 Session-based chat memory
- 📦 Django backend architecture
- 🎨 Custom CSS and JavaScript frontend
- ☁️ GitHub + Vercel CI/CD deployment workflow

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Vercel

### AI Integration
- OpenRouter API
- NVIDIA Nemotron Models

---

# 📂 Project Structure

```bash
chatproject/
│
├── chatapp/
│   ├── migrations/
│   ├── static/
│   │   └── chatapp/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── chat.js
│   │
│   ├── templates/
│   │   └── chatapp/
│   │       └── index.html
│   │
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── chatproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── requirements.txt
├── vercel.json
├── manage.py
└── README.md
```

---

# ⚙️ Local Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/vishnureddy182/chatbot.git
cd chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## 5️⃣ Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# ☁️ Deployment on Vercel

## Push Code to GitHub

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

---

## Connect GitHub Repository to Vercel

1. Login to Vercel
2. Import GitHub repository
3. Configure environment variables
4. Deploy

---

## Required Environment Variables

| Variable | Description |
|---|---|
| OPENROUTER_API_KEY | API key for OpenRouter AI access |

---

# 🔒 Security Notes

Never upload:

- `.env`
- API keys
- database credentials

Use Vercel Environment Variables for production secrets.

---

# 📌 Important Django Production Settings

```python
DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "your-vercel-domain.vercel.app"
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
```

---

# 📦 requirements.txt Example

```txt
Django==5.2.6
openai==2.34.0
requests==2.33.1
python-dotenv==1.2.2
whitenoise==6.12.0
gunicorn==23.0.0
```

---

# 🌟 Future Improvements

- Streaming responses
- Markdown rendering
- PostgreSQL integration
- User authentication
- Chat history database
- RAG integration
- LangChain support
- LangGraph workflows
- AI agent orchestration
- Multi-model support

---

# 👨‍💻 Author

**Vishnu Reddy**

GitHub: https://github.com/vishnureddy182

---

# 📜 License

This project is for educational and portfolio purposes.

