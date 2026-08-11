from src.ingestion.pdf_loader import load_pdf
from src.ingestion.text_splitter import split_text
from src.ingestion.embeddings import get_embeddings

from src.rag.vector_store import (
    create_vector_store,
    load_vector_store
)
from src.rag.retriever import retrieve_documents
from src.rag.qa_chain import (
    create_context,
    create_prompt
)

from src.llm import get_llm
from src.router import get_task

from src.tools.summarize_tool import create_summary_prompt
from src.tools.compare_tool import create_compare_prompt
from src.tools.notes_tool import create_notes_prompt

text = load_pdf("data/AI Engineering.pdf")

chunks = split_text(text)

print("Number of chunks:", len(chunks))

embeddings = get_embeddings()

print("Embedding model loaded successfully")

vector_store = create_vector_store(
    chunks,
    embeddings
)

print("Vector store created successfully")

question = input("Enter your question: ")
task = get_task(question)
print("Question received")

results = retrieve_documents(
    vector_store,
    question
)
print("Documents retrieved")
print("Number of docs:", len(results))

for i, doc in enumerate(results, start=1):
    print(f"\n--- Chunk {i} ---\n")
    print(doc.page_content[:500])

context = create_context(results)
context = context[:3000]
print("Context created")
print("Context length:", len(context))

llm = get_llm()
print("LLM loaded")

if task == "summarize":
    summary_prompt = create_summary_prompt(context)

    print("Sending request to LLM...")

    summary = llm.invoke(summary_prompt)

    print("\nSummary:\n")
    print(summary.content)

elif task == "compare":
    compare_prompt = create_compare_prompt(
        context,
        question
    )

    print("Sending request to LLM...")

    comparison = llm.invoke(compare_prompt)

    print("\nComparison:\n")
    print(comparison.content)

elif task == "notes":
    notes_prompt = create_notes_prompt(
        context,
        question
    )

    print("Sending request to LLM...")

    notes = llm.invoke(notes_prompt)

    print("\nNotes:\n")
    print(notes.content)

else:
    prompt = create_prompt(
        context,
        question
    )

    print("Sending request to LLM...")

    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response.content)
# prompt = create_prompt(
#     context,
#     question
# )

# llm = get_llm()

# response = llm.invoke(prompt)

# print("\nAnswer:\n")
# print(response.content)
