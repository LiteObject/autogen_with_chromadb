import autogen
import chromadb
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import gradio as gr

def autogen_agent_chat(pdf_path, query):

    if not pdf_path:
        return "Please provide a PDF file."

    config_list = [{
        "model": "gpt-3.5-turbo",
    }]

    llm_config_proxy = {
        "temperature": 0,
        "config_list": config_list,
    }

    assistant = AssistantAgent(
        name="my_assistant",
        llm_config=llm_config_proxy,
        system_message="""You are a helpful assistant. Provide accurate answers based on the context. Respond "Unsure about answer" if uncertain."""
    )

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

    user_question = """
    Compose a short blog post showcasing how AutoGen is revolutionizing the future of Generative AI 
    through the collaboration of various agents. Craft an introduction, main body, and a compelling 
    conclusion. Encourage readers to share the post. Keep the post under 500 words.
    """

    user.initiate_chat(
        assistant, problem=user_question,
    )

    # Get the chat messages dictionary associated with the user 
    # object and access the value for the key "assistant".
    messages = user.chat_messages[assistant]

    # In Python "-1" refers to the last element.
    last_message = messages[-1]["content"]

    return last_message

iface = gr.Interface(
    fn=autogen_agent_chat,
    inputs=[
        # gr.File(),
        gr.Textbox(label="URL to PDF", placeholder="Enter the URL to the PDF file"),
        gr.Textbox(label="Blog Topic", placeholder="Enter your blog topic")
    ],
    outputs=gr.Textbox(label="Assistant's Response"),
    title="AutoGen Agent Chat",
    description="Provide a PDF file path to get an answer from the AutoGen Agent",
)

iface.launch()
