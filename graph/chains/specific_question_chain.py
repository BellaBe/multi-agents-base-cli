from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from graph.models import load_model


class SpecificQuestionChain:
    def __init__(self, model_name):
        self.llm = load_model(model_name)
        self.prompt = PromptTemplate.from_template(  
        """
        You are a {role}. Answer this question with step-by-step details: {input}
        """
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def invoke(self, input_data):
        return self.chain.invoke(input_data)
