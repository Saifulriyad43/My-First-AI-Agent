# My First AI Agent

A beginner-friendly AI agent built with LangChain and Groq. It can search the web, count words, and answer questions without any paid API.

This project is designed for complete beginners. If you have never built an AI agent before, you can still get this running in about fifteen minutes.

---

## What This Agent Can Do

- Search the web for current information
- Count words in any text
- Combine multiple tools in one conversation
- Run entirely on free services with no credit card required

---

## Requirements

Before you start, make sure you have:

- Python 3.10 or newer installed
- A free Groq account (sign up at https://console.groq.com)
- A code editor such as VS Code
- Basic ability to open a terminal and type commands

---

## Setup Instructions

Follow these steps in order. Do not skip any.

### Step 1: Get the code

Clone this repository or download it as a zip file and extract it.

```
git clone https://github.com/YOUR_USERNAME/my-first-ai-agent.git
cd my-first-ai-agent
```

### Step 2: Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your computer.

Windows:
```
python -m venv ENV
ENV\Scripts\activate
```

Mac or Linux:
```
python3 -m venv ENV
source ENV/bin/activate
```

You will see `(ENV)` appear at the start of your terminal line. That means it worked.

### Step 3: Install the packages

```
pip install -r requirements.txt
```

### Step 4: Add your API key

Copy the example file:

```
copy .env.example .env
```

On Mac or Linux use `cp .env.example .env` instead.

Open the new `.env` file and replace the placeholder with your real Groq key:

```
GROQ_API_KEY=your_actual_key_here
```

Get your free key from https://console.groq.com under the API Keys section.

### Step 5: Run the agent

```
python agent.py
```

You should see:

```
Building agent...
Agent ready. Type your question or 'exit' to quit.

You:
```

Type a question such as:

```
Search the latest LangChain version and count the words in your answer.
```

The agent will search the web, then count the words, then reply. Press `Ctrl+C` or type `exit` to stop.

---

## Project Structure

```
my-first-ai-agent/
├── agent.py              Main entry point
├── config/
│   └── settings.py       All configuration in one place
├── tools/
│   ├── search.py         Web search tool
│   └── word_count.py     Word counting tool
├── docs/
│   ├── SETUP.md          Detailed setup guide
│   ├── HOW_IT_WORKS.md   Explanation of the agent's logic
│   └── TROUBLESHOOTING.md Common problems and fixes
├── requirements.txt      Python packages needed
├── .env.example          Template for your secret key
└── README.md             This file
```

---

## How It Works in Plain English

An AI agent has four parts.

The brain is a language model. In this project it comes from Groq and runs for free.

The hands are tools. This project has two: one searches the web, the other counts words.

The instructions tell the agent how to behave. They live in `config/settings.py`.

The memory is not included yet. Each question starts fresh. Adding memory is a good next project.

When you ask a question, the agent reads it, decides whether any tool would help, calls those tools, reads the results, and writes a final answer.

For a deeper explanation, read `docs/HOW_IT_WORKS.md`.

---

## Changing the Model

If the model stops working, open `config/settings.py` and change `MODEL_NAME` to another model available on Groq. Good alternatives include `openai/gpt-oss-20b` and `llama-3.1-8b-instant`. You only edit one line.

---

## Common Problems

If something does not work, read `docs/TROUBLESHOOTING.md`. It covers the errors beginners hit most often.

The three most common issues are:

1. Forgetting to activate the virtual environment
2. Forgetting to add the API key to `.env`
3. Using a model name that Groq no longer supports

---

## Next Steps

Once this works, try adding:

- Memory so the agent remembers the conversation
- A calculator tool
- A tool that reads files from your computer
- A streaming mode that shows the agent thinking in real time

Each one teaches a new concept.

---

## License

MIT License. See the LICENSE file for details. You are free to use, modify, and share this project.

---

## Credits

Built as a learning project. Thanks to the LangChain and Groq teams for providing free tools that make projects like this possible.
