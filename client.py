from openai import OpenAI
import os


API_KEY = os.environ.get('OPENAI_API_KEY')

if not API_KEY:
    raise ValueError('API key not found')

client = OpenAI(
    api_key="API_KEY"
)
