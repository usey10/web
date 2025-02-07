from domain.chat.lang_graph.state import GraphState
from typing import Any, Dict
import time
from langgraph.types import StreamWriter

async def delay_node(state: GraphState, writer: StreamWriter) -> Dict[str, Any]:
    time.sleep(3)
    writer(
        {
            "currentNode": "delay_node",
            "sessionId": state["sessionId"],
            "messageId": state["messageId"],
            "answer": "",
            "keywords": [],
            "suggestQuestions": []
        }
    )