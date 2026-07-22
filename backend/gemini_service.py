import os
from dotenv import load_dotenv

load_dotenv()


def generate_answer(context: str, question: str):

    if not context or context.strip() == "":
        return "I couldn't find the answer in the uploaded documents."

    context = context.strip()

    if len(context) > 1800:
        context = context[:1800] + "..."

    return f"""Based on the uploaded documents:

{context}
"""


def generate_cross_analysis(grouped_context):

    if len(grouped_context) < 2:
        return (
            "Only one document contributed to the retrieved answer."
        )

    output = "Comparison of uploaded documents:\n\n"

    for source, chunks in grouped_context.items():

        output += f"📄 {source}\n"

        pages = sorted(
            list(
                {
                    chunk["page"]
                    for chunk in chunks
                }
            )
        )

        output += f"Relevant Pages: {pages}\n"

        preview = ""

        for chunk in chunks:
            preview += chunk["text"][:150] + " "

        output += preview[:350]
        output += "\n\n"

    output += (
        "\nConclusion:\n"
        "The retrieved information above comes directly from the uploaded PDFs."
    )

    return output