import argparse
import cmd
from graph import create_graph, MODELS_MAP

from dotenv import load_dotenv

load_dotenv()


class CLIApp(cmd.Cmd):
    intro = 'Welcome to the Agent CLI. Type help or ? to list commands.\n'
    prompt = '(agent-cli) '
    field_of_expertise = None
    role = None
    model_name = None

    def do_set_expertise(self, arg):
        'Set the field of expertise: set_expertise <expertise>'
        self.field_of_expertise = arg
        print(f"Field of expertise set to: {self.field_of_expertise}")

    def do_set_role(self, arg):
        'Set the role: set_role <role>'
        self.role = arg
        print(f"Role set to: {self.role}")

    def do_set_model(self, arg):
        'Set the model: set_model <model_name>'
        if arg in MODELS_MAP:
            self.model_name = arg
            print(f"Model set to: {self.model_name}")
        else:
            print(
                f"Model {arg} is not recognized. Available models are: {', '.join(MODELS_MAP.keys())}")

    def do_ask(self, arg):
        'Ask a question: ask <question>'
        if self.field_of_expertise and self.role and self.model_name:
            state = {
                "input": arg,
                "continue_conversation": True,
                "field_of_expertise": self.field_of_expertise,
                "role": self.role,
                "model_name": self.model_name
            }
            graph = create_graph()
            result = graph.invoke(state)
            print("\n---Final Answer---")
            print(result["answer"])
        else:
            print("Please set field of expertise, role, and model before asking questions.")


    def do_change_settings(self, arg):
        'Change field of expertise, role, and model'
        self.do_set_expertise(input('What field of expertise should the agent have? '))
        self.do_set_role(input('What role should the agent assume? '))
        self.do_set_model(input('What model should the agent use? '))

    def preloop(self):
        self.do_change_settings('')

    def do_exit(self, arg):
        'Exit the CLI'
        print('Thank you for using Agent CLI.')
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Agent CLI Application')
    args = parser.parse_args()
    CLIApp().cmdloop()
