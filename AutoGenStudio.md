# AutoGen Studio Overview

AutoGen Studio is like a Lego set for AI agents. It lets you build teams of AI helpers without needing to code. You can design what each agent does, how they interact, and even train them on specific tasks. Think of it as simplifying complex AI systems into an intuitive interface.

## Create a virtual environment
    virtualenv -p python3.11 .venv

## Activate the virtual environment
    .venv/scripts/activate

## Set OpenAI API Key as an environment variable
    export OPENAI_API_KEY=XXXXXXXXXXX

The PowerShell command looks like this `$Env:OPENAI_API_KEY="XXXXXXXXXXX"`

## Install AutoGen Studio
    pip install autogenstudio

## Run AutoGen Studio
    autogenstudio ui --port 8081 >> output.txt

## Some of the main components of AutoGen Studio

### Build Section:
- **Agent creation**: Define different AI agents with unique names, descriptions, and characteristics.
- **Skill definition**: Design specific skills for each agent, outlining their functionalities and responses.
- **Workflow configuration**: Build interconnected workflows outlining how agents interact and respond to prompts or situations.
- **Training**: Train your agents on specific tasks using provided datasets or custom data.

### Playground Section:
- **Interactive testing**: Experiment with your created agents in real-time, sending prompts and observing their responses.
- **Debugging and refinement**: Identify and fix issues in your agent's behavior based on their responses in the playground.
- **Exploring capabilities**: Test and understand the different functions and skills of your agents in a controlled environment.

### Gallery Section:
- **Pre-built agents and skills**: Access a library of community-created agents and skills, saving time and effort.
- **Sharing creations**: Contribute your own agents and skills to the wider community, fostering collaboration and learning.
- **Inspiration and learning**: Discover new possibilities and approaches by exploring other users' works in the gallery.

### Additional components:
- **LLM Providers and API Keys**: Connect to different Language Learning Models (LLMs) like OpenAI or Azure for advanced text generation and comprehension.
- **Python API**: For more advanced users, a programmatic API allows deeper control over agent creation and workflow management.

Overall, these components work together to provide a user-friendly platform for building and experimenting with multi-agent AI systems, even without extensive coding knowledge.


---
## Links

### X-Force IDE
>X-Force IDE is a low code agent as a service UI framework that lets you to create agent based workforces from drag and drop like user interface. 
- [X-Force IDE](https://x-force.notion.site/Introduction-to-X-Force-IDE-b92c434802de4df6a58c83fd5d292c33)

### LM Studio
>This LM Studio is a free, open-source application that allows you to run large language models (LLMs) locally on your own computer. 
- [LM Studio](https://lmstudio.ai/)

### LiteLLM
LiteLLM is an open-source library that makes it easier to use various large language models (LLMs) like GPT-3, Jurassic-1 Jumbo, and Bard. You can call all LLM APIs using the OpenAI format.

>Call 100+ LLMs using the same Input/Output Format

- [LiteLLM - Getting Started](https://docs.litellm.ai/)