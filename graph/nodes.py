from graph.state import AgentState
from graph.chains import RouterChain, SpecificQuestionChain, GenericQuestionChain


def route_question(state: AgentState) -> AgentState:
    model_name = state["model_name"]
    chain = RouterChain(model_name)
    decision = chain.invoke(
        {"input": state["input"], "field_of_expertise": state["field_of_expertise"]})
    state["decision"] = decision.lower()
    print(f"Decision: {decision}")
    return state


def answer_specific_question(state: AgentState) -> AgentState:
    model_name = state["model_name"]
    chain = SpecificQuestionChain(model_name)
    answer = chain.invoke({"input": state["input"], "role": state["role"]})
    state["answer"] = answer
    return state


def answer_general_question(state: AgentState) -> AgentState:
    model_name = state["model_name"]
    chain = GenericQuestionChain(model_name)
    answer = chain.invoke({"input": state["input"]})
    state["answer"] = answer
    return state
