import logging
import os

from openai import OpenAI

from app.chat.system_prompt import SYSTEM_PROMPT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_message(message: str):
    stream = client.responses.create(
        model=os.getenv("LLM_MODEL"),
        instructions=SYSTEM_PROMPT,
        input=message,
        max_output_tokens=200,
        stream=True,
    )

    for event in stream:
        logger.info("Event: %s", event.type)

        if event.type == "response.output_text.delta":
            logger.info("Chunk: %r", event.delta)
            yield event.delta

        elif event.type == "response.incomplete":
            reason = event.response.incomplete_details.reason

            logger.info(
                "Response incomplete: %s",
                reason,
            )

            if reason == "max_output_tokens":
                yield "\n[RESPONSE_TRUNCATED]"

        elif event.type == "response.completed":
            usage = event.response.usage

            logger.info(
                "Token usage - input: %s, output: %s, total: %s",
                usage.input_tokens,
                usage.output_tokens,
                usage.total_tokens,
            )
