import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from ddgs import DDGS

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)


@tool
def web_search(query: str) -> str:
    """Search the web for the given query and return top results."""
    results = DDGS().text(query, max_results=3)
    if not results:
        return "No results found."
    output = []
    for r in results:
        output.append(f"{r['title']}: {r['body']}")
    return "\n\n".join(output)


@tool
def word_count(text: str) -> int:
    """Count how many words are in the text."""
    return len(text.split())


tools = [web_search, word_count]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant."
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "Search the latest LangChain version, then tell me how many words your answer has."}
    ]
})

print(result["messages"][-1].content)