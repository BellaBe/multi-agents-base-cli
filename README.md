# Agent CLI Application

This is a command-line interface (CLI) application that allows users to interact with an AI agent. The agent can be configured with a specific field of expertise, role, and model for answering questions.

## Features

- Set the field of expertise for the agent.
- Set the role the agent should assume.
- Select the AI model to use for answering questions.
- Ask questions and receive answers based on the configured settings.
- Change settings at any time during the session.

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/agent-cli-application.git
cd agent-cli-application
```

2. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a .env file in the project root directory and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```


## Usage
To start the CLI application, run the following command:

```
python main.py
```

Upon starting, you will be prompted to set the following:

1. Field of expertise: The area of knowledge the agent should have.
2. Role: The role the agent should assume.
3. Model: The AI model to use for answering questions.
Example session:

```
Welcome to the Agent CLI. Type help or ? to list commands.

What field of expertise should the agent have? Python programming
What role should the agent assume? Software Engineer
What model should the agent use? gpt-4-turbo
(agent-cli) ask How do I create a virtual environment in Python?
---Final Answer---
To create a virtual environment in Python, you can use the following command:
...
(agent-cli) exit
Thank you for using Agent CLI.
```

## Available Models
The following models are available for selection:

- gpt-4o
- gpt-4-turbo
- gpt-4
- gpt-3.5-turbo
- gemma-7b-it
- gemma2-9b-it
- llama3-70b-8192
- llama3-8b-8192
- mixtral-8x7b-32768

## Commands
- set_expertise <expertise>: Set the field of expertise.
- set_role <role>: Set the role.
- set_model <model_name>: Set the model.
- ask <question>: Ask a question.
- change_settings: Change the field of expertise, role, and model.
- exit: Exit the CLI.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License
This project is for learning purposes and can be used by anyone. There are no restrictions on its use.