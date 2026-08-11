from langchain_ollama import ChatOllama


def get_llm():
    llm = ChatOllama(
        model="phi4-mini:3.8b",
        temperature=0
    )

    return llm