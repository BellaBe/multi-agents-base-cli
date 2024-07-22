from typing import TypedDict


class AgentState(TypedDict):
    field_of_expertise: str
    role: str
    input: str
    decision: str
    answer: str
    continue_conversation: bool
    model_name: str
