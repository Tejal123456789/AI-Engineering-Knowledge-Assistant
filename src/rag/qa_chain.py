def create_context(results):
    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    return context


def create_prompt(context, question):
    prompt = f"""
You are an AI Engineering Assistant.

Rules:
1.Answer only from the provided context.
2.Do not use your own knowledge.
3.If the answer is not present in the context, say:
 "I could not find this information in the provided documents."
4.Be concise and accurate.

Context:
{context}

Question:
{question}

Answer:
"""
    
    return prompt