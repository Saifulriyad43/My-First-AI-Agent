# How the Agent Works

This document explains what is happening inside the agent in plain English.

---

## The Four Parts of an Agent

Every AI agent has four parts.

The brain is a language model. It reads text and writes text. In this project the brain lives on Groq's servers and runs for free.

The hands are tools. A tool is just a Python function with a description attached. The description tells the brain what the tool does so the brain knows when to use it.

The instructions are a system prompt. This is a short message that shapes how the brain behaves. For example, telling it to be concise or to always search before answering.

The memory is optional. Without it, each question starts fresh with no knowledge of the last one. This project does not include memory yet.

---

## What Happens When You Ask a Question

Step 1: Your question is sent to the brain along with the list of available tools.

Step 2: The brain reads the question and the tool descriptions. It decides whether any tool would help.

Step 3: If a tool is needed, the brain writes a command asking to run it. For example, it might say "run web_search with the query 'latest LangChain version'".

Step 4: The tool runs and returns its result.

Step 5: The result is sent back to the brain.

Step 6: The brain may decide another tool is needed. If so, steps 3 through 5 repeat.

Step 7: When the brain has enough information, it writes a final answer in plain English.

Step 8: The answer is returned to you.

---

## Why the Tool Description Matters

The brain chooses tools based on their descriptions. If a description is vague, the brain may use the wrong tool or skip it entirely.

A good description says exactly what the tool does and when to use it.

Compare these two descriptions for a search tool:

Bad: "Searches things."

Good: "Search the web for current information. Use this when the question involves recent events, versions, prices, or anything that changes over time."

The second description gives the brain clear guidance. This is why the docstring in `tools/search.py` is written carefully.

---

## Why Temperature Is Set to Zero

Temperature controls randomness. At zero, the brain always picks the most likely next word, which makes answers consistent and predictable. This is good for tool use because you want the agent to reliably choose the right tool.

If you set temperature to one, the agent becomes more creative but also more likely to make mistakes. For a tool-using agent, zero is usually best.

---

## What LangChain Does

LangChain is a library that connects brains, tools, and instructions together. Without it, you would write all the plumbing yourself. With it, you write a few lines.

The key function is `create_agent`. You give it a model, a list of tools, and a system prompt. It returns an agent that handles the entire loop of thinking, acting, and answering.

---

## What Groq Does

Groq runs large language models on special hardware that makes them respond very quickly. They offer a free tier that is generous enough for learning and small projects. No credit card required.

You get an API key from their website, put it in `.env`, and your code uses it to send questions to their servers.

---

## What Happens If a Tool Fails

If a tool raises an error, the error message is sent back to the brain as the tool's result. The brain then decides what to do. Often it will try a different approach or explain the problem in its answer. This is why the search tool catches exceptions and returns a readable message instead of crashing.