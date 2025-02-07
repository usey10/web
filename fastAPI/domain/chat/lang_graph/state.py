from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class GraphState(TypedDict):
    sessionId: int
    messageId: int
    current_node: str
    question: str
    generation: str
    messages: Annotated[list, add_messages]