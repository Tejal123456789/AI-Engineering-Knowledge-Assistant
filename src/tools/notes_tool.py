def create_notes_prompt(context, question):
    prompt = f"""
You are an AI Engineering Assistant.

Create well-structured study notes using only the provided context.

Rules:
1. Use only the provided context.
2. Organize notes using headings and bullet points.
3. Include key concepts.
4. Include important takeaways.
5. If enough information is not available, say so.

Context:
{context}

User Request:
{question}

Notes:
"""

    return prompt