import streamlit as st
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.text_splitter import split_text
from src.ingestion.embeddings import get_embeddings
from src.rag.vector_store import create_vector_store
from src.rag.retriever import retrieve_documents
from src.rag.qa_chain import create_context, create_prompt
from src.llm import get_llm
from src.router import get_task
from src.tools.summarize_tool import create_summary_prompt
from src.tools.compare_tool import create_compare_prompt
from src.tools.notes_tool import create_notes_prompt

st.set_page_config(
    page_title="AI Engineering Assistant",
    layout="wide"
)

st.title("AI Engineering Knowledge Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []

st.caption(
    "RAG-powered assistant for answering questions, generating summaries, creating notes, and comparing AI concepts."
)
with st.sidebar:
    st.header("Project Information")

    st.write("AI Engineering Assistant")

    st.write("Capabilities:")
    st.write("- Question Answering")
    st.write("- Summarization")
    st.write("- Comparison")
    st.write("- Notes Generation")

    st.write("Knowledge Base:")
    st.write("11 AI/ML Books")

# Backend Initialization
text = load_pdf("data/AI Engineering.pdf")
chunks = split_text(text)
embeddings = get_embeddings()
vector_store = create_vector_store(
    chunks,
    embeddings
)

st.markdown(
    """
    Ask questions, generate summaries, create notes,
    and compare concepts using your engineering knowledge base.
    """
)

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask your question"
)

if question:
    st.session_state.messages.append(
    {
        "role": "user",
        "content": question
    }
)

    with st.chat_message("user"):
        st.markdown(question)
    st.divider()

    task = get_task(question)
    st.subheader("Detected Task")
    st.info(task.upper())

    results = retrieve_documents(
        vector_store,
        question
    )

    context = create_context(results)

    llm = get_llm()

    if task == "summarize":

        prompt = create_summary_prompt(context)

        response = llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.content)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )
    elif task == "compare":

        prompt = create_compare_prompt(
            context,
            question
        )

        response = llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.content)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

    elif task == "notes":

        prompt = create_notes_prompt(
            context,
            question
        )

        response = llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.content)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

    else:

        prompt = create_prompt(
            context,
            question
        )

        response = llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.content)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )