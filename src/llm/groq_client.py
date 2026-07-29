from groq import Groq

from src.config import GROQ_API_KEY, MODEL_NAME


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, question: str, context: str) -> str:
        prompt = f"""
You are a technical support assistant.

Use ONLY the provided manual context to answer.

Manual Context:
{context}

User Question:
{question}

Provide:
1. Step-by-step instructions.
2. Be concise.
3. If the answer is not in the context, say you don't know.
"""

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content