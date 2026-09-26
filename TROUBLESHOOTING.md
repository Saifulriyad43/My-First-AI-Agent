# Troubleshooting Guide

If something breaks, find the error message below and follow the fix.

---

## Error: `python: command not found`

Python is not installed or not on your PATH.

Fix: Download Python from https://python.org. On Windows, during installation, check "Add Python to PATH". Restart your terminal afterward.

---

## Error: `(ENV)` does not appear in the terminal

The virtual environment is not activated.

Fix: Run the activation command again.

Windows:
```
ENV\Scripts\activate
```

Mac or Linux:
```
source ENV/bin/activate
```

---

## Error: `ModuleNotFoundError: No module named 'langchain'`

The packages are not installed, or you installed them outside the virtual environment.

Fix: Activate the environment first, then install.

```
ENV\Scripts\activate
pip install -r requirements.txt
```

---

## Error: `GROQ_API_KEY is missing`

The `.env` file is missing or does not contain your key.

Fix: Copy `.env.example` to `.env` and paste your real key inside. Make sure there are no spaces around the equals sign.

Correct:
```
GROQ_API_KEY=gsk_abc123
```

Wrong:
```
GROQ_API_KEY = gsk_abc123
```

---

## Error: `model_not_found` or `does not exist`

Groq has retired the model you are using.

Fix: Open `config/settings.py` and change `MODEL_NAME` to a model Groq currently supports. Check https://console.groq.com/docs/models for the current list. Good choices are `openai/gpt-oss-120b` and `openai/gpt-oss-20b`.

---

## Error: `401 Unauthorized`

Your API key is wrong or has been deleted.

Fix: Go to https://console.groq.com, create a new key, and replace the old one in `.env`.

---

## Error: `Rate limit exceeded`

You have sent too many requests in one day.

Fix: Wait until the next day, or switch to a model with a higher daily limit in `config/settings.py`.

---

## Error: `Could not import ddgs`

The search package is missing.

Fix:
```
pip install -U ddgs
```

---

## The agent answers but does not use any tools

The brain decided tools were not needed. This often happens when the question does not clearly require current information.

Fix: Rephrase your question to make the tool obviously useful. For example, instead of "What is LangChain?", ask "Search the web for the latest LangChain version".

---

## The agent gives a wrong answer

Language models sometimes make mistakes. This is normal.

Fix: Ask again with more specific wording. If the answer involves current facts, make sure the agent used the search tool by checking whether the response mentions recent information.

---

## Nothing works and you are stuck

Try these in order.

1. Close the terminal and open a new one.
2. Activate the environment again.
3. Run `pip install -r requirements.txt` again.
4. Check that `.env` contains your key with no spaces.
5. Check that `config/settings.py` uses a current model name.
6. Read the full error message. The last line usually says exactly what is wrong.

If you are still stuck, open an issue on GitHub with the full error message and what you tried.