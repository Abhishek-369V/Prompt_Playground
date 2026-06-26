# 🧪 Prompt Playground

> 🔖 **Learning Project** | Prompt Engineering Practice | Streamlit + OpenAI

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)

---

## 📌 About

A hands-on learning project built while studying **Prompt Engineering**.  
The app lets users experiment with different roles, tasks, constraints, and response lengths — and directly observe how changing prompt variables changes LLM output. Built to understand the core principle:

> **Changing the prompt → Changes the output. Not the model.**

---

## ✨ Features

- Select AI role — Teacher, Interviewer, Technical Writer, Friendly Assistant
- Select task — Explain, Summarize, Generate, Rewrite
- Select constraint — Simple Language, Bullet Points, Examples, Professional Tone
- Control response length — Short, Medium, Detailed
- Shows **constructed prompt** before the response (full transparency)
- Input validation — no empty queries

---

## 🧠 What I Learned

- How prompt variables (role, task, constraint) affect model output
- Role prompting and constraint prompting techniques
- Dynamic prompt template construction
- UI/Backend separation pattern in Streamlit apps
- Observing output differences without changing the model

---

## 🗂️ Project Structure

```
prompt_playground/
├── app.py          # Streamlit UI
├── backend.py      # Prompt builder + OpenAI API call
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend UI |
| OpenAI API (GPT-4o-mini) | Response generation |

---

## 🔍 Core Concept

```
User selects: Role + Task + Constraint + Length + Query
                          ↓
              Prompt is built dynamically
                          ↓
              Same model, different instructions
                          ↓
              Completely different output
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/prompt-playground.git
cd prompt-playground

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
# Create .streamlit/secrets.toml and add: "your-key-here"

# 4. Run
streamlit run app.py
```

---


## 📈 Possible Extensions

- [ ] Add temperature slider
- [ ] Add copy prompt button
- [ ] Store prompt history across sessions
- [ ] Add prompt templates library
- [ ] Compare outputs side by side (two models)

---

## 👨‍💻 Author

**Abhishek** — B.Tech CSE | AI/ML Enthusiast  
[GitHub](https://github.com/Abhishek-369V) • [LinkedIn](https://www.linkedin.com/in/madanala-abhishek-varma/)
