from gemini_client import generate_content


def explain_concept(topic: str) -> str:
    prompt = f"""
Explain the following concept in simple English.

Topic:
{topic}

Rules:
- Explain clearly.
- Use simple English.
- Give a short example.
- Keep the answer easy for a student to understand.
"""

    return generate_content(prompt)