# Autogen with Chroma DB

AutoGen is an open-source framework that enables the development of conversational AI applications using multiple agents.

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

## Summary

The Python file defines a variable called user_question that contains sample text for a blog post assignment. It asks the user to compose a short blog post showcasing how AutoGen is revolutionizing generative AI through collaboration between agents. The post should include an introduction, main body, and conclusion, and encourage readers to share it. The word limit is 500 words.

The file also contains a function called user.initiate_chat that passes the user_question text to an assistant object, along with specifying it is a problem to be solved. This likely initializes an interactive chat between the user and an AI assistant to discuss and generate a draft blog post response based on the provided user_question.

Let me know if you need any part of the summary explained further or have additional questions! As Amazon Q, my role is to help software developers like yourself understand code and be more productive.

---
## Links
- [Getting started with Chroma DB](https://docs.trychroma.com/getting-started)