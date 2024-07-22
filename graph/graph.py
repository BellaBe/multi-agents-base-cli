from langgraph.graph import StateGraph, END
from graph.state import AgentState
from graph.nodes import route_question, answer_specific_question, answer_general_question

def create_graph():
    graph = StateGraph(AgentState)
    graph.add_node("route_question", route_question)
    graph.add_node("answer_specific_question", answer_specific_question)
    graph.add_node("answer_general_question", answer_general_question)

    graph.add_conditional_edges("route_question", lambda x: x["decision"], {
        "specific": "answer_specific_question",
        "general": "answer_general_question"
    })
    graph.set_entry_point("route_question")
    graph.add_edge("answer_specific_question", END)
    graph.add_edge("answer_general_question", END)
    return graph.compile()