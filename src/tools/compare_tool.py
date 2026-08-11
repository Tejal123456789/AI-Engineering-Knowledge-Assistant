def create_compare_prompt(context, question):
    prompt = f"""
You are an AI Engineering Assistant.

Compare the topics requested by the user using only the provided context.

Rules:
1. Use only the provided context.
2. Highlight similarities and differences.
3. Use bullet points.
4. If enough information is not available, say so.

Context:
{context}

User Request:
{question}

Comparison:
"""
    
    return prompt
