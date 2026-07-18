from llm.config import llm
from llm.prompts import ANSWER_PROMPT

def generate_answer(question, context):
    prompt = ANSWER_PROMPT.format(
    context=context,
    question=question
)

    response = llm.invoke(prompt)
    return response.text