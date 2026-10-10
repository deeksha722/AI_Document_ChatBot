import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found in the .env file."
    )

groq_client = Groq(api_key=api_key)


def generate_answer(question, context, chat_history=None):
    """
    Generate an answer using Groq and retrieved PDF context.
    """

    if chat_history is None:
        chat_history = []

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI document assistant. "
                "Answer questions using the provided document context. "
                "If the answer is not supported by the context, "
                "say that the uploaded document does not provide "
                "enough information. "
                "Explain concepts clearly and simply. "
                "Use previous conversation messages to understand "
                "follow-up questions, but do not invent facts."
            )
        }
    ]

    # Include earlier messages to help with follow-up questions.
    messages.extend(chat_history[-6:])

    messages.append(
        {
            "role": "user",
            "content": (
                f"Relevant document context:\n{context}\n\n"
                f"Question: {question}"
            )
        }
    )

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer