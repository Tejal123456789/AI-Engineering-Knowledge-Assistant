def retrieve_documents(vector_store, query):
    results = vector_store.max_marginal_relevance_search(
        query,
        k=5,
        fetch_k=10
    )

    return results