from gemini_client import generate_content


def generate_notes(topic: str) -> str:

    prompt = f"""
You are EduGenie, an AI educational assistant.

Create clear and useful study notes for the following topic:

Topic:
{topic}

Follow this format:

# Study Notes

## 1. Introduction
Give a simple introduction to the topic.

## 2. Key Points
List the most important points.

## 3. Important Terms
Explain important terms in simple language.

## 4. Examples
Give simple examples where useful.

## 5. Quick Revision
Give short points that a student can quickly revise before an exam.

Instructions:
- Use simple English.
- Keep the explanation beginner-friendly.
- Use headings and bullet points.
- Do not add unnecessary information.
- Make the notes useful for students.
"""

    return generate_content(prompt)