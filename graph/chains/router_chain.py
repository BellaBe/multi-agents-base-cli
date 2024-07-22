from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from graph.models import load_model


class RouterChain:
    def __init__(self, model_name):
        self.llm = load_model(model_name)
        self.prompt = PromptTemplate.from_template(
            """
        You are an agent that needs to define if a question is {field_of_expertise} one or a general one.

        Question: {input}

        Analyse the question. Only answer with "specific" if the question is about {field_of_expertise}. If not, just answer "general". 

        Your answer (specific/general):
        """
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def invoke(self, input_data):
        return self.chain.invoke(input_data)
