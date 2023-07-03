import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_openai_api_key():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        key_file = os.path.join(os.path.expanduser("~"),".openai-api-key.txt")
        api_key = open(key_file).read().strip()

    return api_key