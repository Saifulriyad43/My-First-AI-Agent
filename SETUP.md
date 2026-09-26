# Detailed Setup Guide

This document walks through setup very slowly. If the README was enough, you do not need this. If you got stuck, read on.

---

## Check Your Python Version

Open a terminal and type:

```
python --version
```

You should see something like `Python 3.11.5`. If you see an error, Python is not installed. Download it from https://python.org and during installation on Windows, check the box that says "Add Python to PATH".

---

## Opening a Terminal

On Windows, press the Windows key, type `cmd`, and press Enter.

On Mac, press Command and Space, type `terminal`, and press Enter.

---

## What a Virtual Environment Is

Imagine your computer has one big box of Python packages. Every project you make shares that box. Soon projects start conflicting because one needs version 1 of a package and another needs version 2.

A virtual environment is a small separate box for one project. Nothing inside touches the outside.

That is why we run `python -m venv ENV` before installing anything.

---

## Activating the Environment

After creating it, you must activate it every time you open a new terminal to work on this project.

Windows:
```
ENV\Scripts\activate
```

Mac or Linux:
```
source ENV/bin/activate
```

You will know it worked when you see `(ENV)` at the start of your terminal prompt.

If you close the terminal, you must activate it again next time. It does not stay on.

---

## Getting the Groq API Key

Go to https://console.groq.com

Sign up with your email. No credit card is required.

Once you are logged in, find the API Keys section in the sidebar.

Click "Create API Key". Give it any name, such as "my-first-agent".

Copy the key. It starts with `gsk_`.

Paste it into your `.env` file after `GROQ_API_KEY=`.

Important: never share this key or upload it to GitHub. Treat it like a password.

---

## Running the Agent

Make sure you are in the project folder. The path shown in your terminal should end with `my-first-ai-agent`.

Make sure the virtual environment is activated. You should see `(ENV)`.

Run:

```
python agent.py
```

If you see the prompt `You:`, everything worked.

---

## Asking Good Questions

The agent decides which tools to use based on your question. To see the tools in action, ask questions that clearly need them.

To trigger web search:
```
What is the latest Python version?
```

To trigger word count:
```
How many words are in this sentence?
```

To trigger both:
```
Search for the latest LangChain release and tell me how many words your answer has.
```

If the agent does not use a tool, try rephrasing your question to make the tool more obviously useful.