from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from graph.models import load_model


class GenericQuestionChain:
    def __init__(self, model_name):
        self.llm = load_model(model_name)
        self.prompt = PromptTemplate.from_template(
            """
        Your are a helpful assistant. Give a general and concise answer to the question: {input}
        """
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def invoke(self, input_data):
        return self.chain.invoke(input_data)
