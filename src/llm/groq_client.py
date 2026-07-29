from groq import Groq

from src.config import GROQ_API_KEY, MODEL_NAME


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(
        self,
        question: str,
        context: str,
        image_caption: str | None = None,
    ) -> str:

        prompt = f"""
You are a technical support assistant.

Use ONLY the provided manual context and image description to answer.

Manual Context:
{context}
"""

        if image_caption:
            prompt += f"""

Image Description:
{image_caption}
"""

        prompt += f"""

User Question:
{question}

Instructions:
1. Use both the manual context and the image description if relevant.
2. Give clear step-by-step troubleshooting instructions.
3. If the answer is not supported by the provided information, say you don't know.
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