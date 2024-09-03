from langchain_openai import ChatOpenAI
from utils.helper_functions import load_config
import os

config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
load_config(config_path)


def get_open_ai(temperature=0, model='gpt-3.5-turbo'):

    llm = ChatOpenAI(
    model=model,
    temperature = temperature,
    base_url="https://api.302.ai/v1/chat/completions",
)
    return llm

# Return json format
def get_open_ai_json(temperature=0, model='gpt-3.5-turbo'):
    llm = ChatOpenAI(
    model=model,
    temperature = temperature,
    model_kwargs={"response_format": {"type": "json_object"}},
    base_url="https://api.302.ai/v1/chat/completions",
)
    return llm
