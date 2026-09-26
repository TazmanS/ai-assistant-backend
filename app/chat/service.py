import logging
import os

from openai import OpenAI

from app.chat.system_prompt import SYSTEM_PROMPT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_message(message: str) -> str:
    logger.info("Processing chat message")
    response = client.responses.create(
        model=os.getenv("LLM_MODEL"),
        instructions=SYSTEM_PROMPT,
        input=message,
        max_output_tokens=100,
    )

    usage = response.usage

    logger.info(
        "Token usage - input: %s, output: %s, total: %s",
        usage.input_tokens,
        usage.output_tokens,
        usage.total_tokens,
    )
    return response.output_text
