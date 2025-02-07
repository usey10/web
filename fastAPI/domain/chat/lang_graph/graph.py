from langgraph.graph import START, END, StateGraph
from domain.chat.lang_graph.state import GraphState
from domain.chat.lang_graph.generate import generate
from domain.chat.lang_graph.delay_node import delay_node

workflow = StateGraph(GraphState)

workflow.add_node("chatbot", generate)
workflow.add_node("delay_node", delay_node)

workflow.add_edge(START, "delay_node")
workflow.add_edge("delay_node", "chatbot")
workflow.add_edge("chatbot", END)

graph_app = workflow.compile()