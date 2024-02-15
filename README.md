# Autogen with Chroma DB

>AutoGen is an open-source framework that enables the development of conversational AI applications using multiple agents.

>Chroma DB is an open-source vector database for storing and retrieving vector embeddings.

### Create virtual python environment
- `virtualenv -p python3.11 env_name`
- `python -m venv env_name`

### Activate the virtual env
- `env_name/scripts/activate`

---
## Installs AutoGen & Chroms DB
    pip install -U "pyautogen[retrievechat]" chromadb


- `-U` tells pip to upgrade any already installed packages to their latest versions before installing.
- `"pyautogen[retrievechat]"` installs the pyautogen package and also installs the optional "retrievechat" extra feature of that package

## Set environment variable AUTOGEN_USE_DOCKER to False

### Bash Command:
    export AUTOGEN_USE_DOCKER=False


### PowerShell Command:
    $Env:AUTOGEN_USE_DOCKER="False"


Exporting `AUTOGEN_USE_DOCKER=False` tells pyautogen to run its tasks directly on the host rather than using Docker containers. It bypasses the Docker dependency but also loses some of the isolation benefits Docker provides.

## Set environment variable OPENAI_API_KEY=???

### Bash Command:
    export OPENAI_API_KEY=Fxxxxxxxxxxxxxxxxxxxxxxxxx

### PowerShell Command:
    $Env:OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxx"


## Run `app.py`
    python app.py

## Explanation of the code file

This code file defines a chatbot system using the autogen and chromadb libraries. Here's a step-by-step breakdown of the code:

### Importing Libraries
The first step is to import the necessary libraries. In this case, we're using autogen and chromadb to create a chatbot that can retrieve information from a database and generate responses based on a language model.

```python
import autogen
import chromadb
```

### Defining the Chatbot Assistant
Next, we define the chatbot assistant using the AssistantAgent class from the autogen library. This class takes a name, language model configuration, and system message as input.

```python
assistant = AssistantAgent(
    name="my_assistant",
    llm_config=llm_config_proxy,
    system_message="You are a helpful assistant. Provide accurate answers based on the context. Respond 'Unsure about answer' if uncertain."
)
```
### Defining the User
We also define the user using the RetrieveUserProxyAgent class from the autogen.agentchat.contrib module. This class takes a name, human input mode, system message, maximum number of consecutive auto-replies, and configuration for retrieving information from a database as input.

```python
user = RetrieveUserProxyAgent(
    name="me_user",
    human_input_mode="NEVER",
    system_message="Assistant who has extra content retrieval power for solving difficult problems.",
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "code",
        "docs_path": ['./docs/autogen.pdf'],
        "chunk_token_size": 1000,
        "model": config_list[0]["model"],
        "client": chromadb.PersistentClient(path='/tmp/chromadb'),
        "collection_name": "pdfreader",
        "get_or_create": True,
    },
    code_execution_config={"work_dir": "coding"},
)
```

### Defining the User Question
We define the user's question or prompt as a string variable.

```python
user_question = """
Compose a short blog post showcasing how AutoGen is revolutionizing the future of Generative AI 
through the collaboration of various agents. Craft an introduction, main body, and a compelling 
conclusion. Encourage readers to share the post. Keep the post under 500 words.
"""
```

### Initiating the Chat
Finally, we initiate the chat session between the user and the chatbot using the initiate_chat method of the RetrieveUserProxyAgent class.

```python
user.initiate_chat(assistant, problem=user_question)
```

### Summary
Overall, this code file defines a chatbot system that can respond to user questions or prompts by retrieving information from a database and generating responses based on a language model. The chatbot can also execute code and provide answers based on the context of the user's question.

---
## Links
- [Getting started with Chroma DB](https://docs.trychroma.com/getting-started)
- [AutoGen: Enable Next-Gen Large Language Model Applications](https://microsoft.github.io/autogen/)