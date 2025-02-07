from dotenv import load_dotenv
from openai import AsyncOpenAI
from domain.chat.lang_graph.state import GraphState

from typing import Any, Dict

from langgraph.types import StreamWriter

load_dotenv(dotenv_path=".env", override=True)

# client = OpenAI()
client = AsyncOpenAI()


async def generate(state: GraphState, writer: StreamWriter) -> Dict[str, Any]:
    question = state["question"]
    # documents = state["documents"]

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{question}"}],
        stream=True,
    )

    chunks = []
    current_node = "generate"
    async for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            writer(
                {
                    "currentNode": current_node,
                    "sessionId": state["sessionId"],
                    "messageId": state["messageId"],
                    "answer": chunk.choices[0].delta.content,
                    "keywords": [],
                    "suggestQuestions": []
                }
            )

            chunks.append(
                {
                    "chunk": chunk.choices[0].delta.content,
                    "current_node": current_node
                }
            )
        else:
            writer(
                {
                    "currentNode": current_node,
                    "sessionId": state["sessionId"],
                    "messageId": state["messageId"],
                    "answer": "",
                    "keywords": ["DSLR", "ISO", "AF/MF"],
                    "suggestQuestions": ["temp suggestQuestion 1", "temp suggestQuestion 2", "temp suggestQuestion 3"]
                }
            )
    return {"question": question, "generation": "".join(chunks)}