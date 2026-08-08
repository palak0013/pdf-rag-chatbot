def rag_pipeline(query, retriever, client):

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

Rules:

- Never use outside knowledge.
- Never hallucinate.
- If the answer is missing, say:

"I couldn't find that information in the uploaded documents."

- Use Markdown.
- Use headings and bullet points when useful.

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text, docs