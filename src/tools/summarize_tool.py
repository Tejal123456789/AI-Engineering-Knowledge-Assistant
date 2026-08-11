def create_summary_prompt(context):
    prompt = f"""
You are an AI Engineering Assistant.

Summarize the following content.

Rules:
1. Use only the provided content.
2. Keep the summary concise.
3. Highlight the most important concepts.
4. Use bullet points.

Content:
{context}

Summary:
"""
    
    return prompt