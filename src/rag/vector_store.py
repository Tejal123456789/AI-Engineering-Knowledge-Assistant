import os
from langchain_chroma import Chroma


VECTOR_DB_PATH = "vectorstore"


def create_vector_store(chunks, embeddings):
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store


def load_vector_store(embeddings):
    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    return vector_store