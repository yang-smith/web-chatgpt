import openai
import os

api_key = os.environ.get("API_KEY")

openai.api_key = api_key

def create_chat_completion(content, model_name):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ],
        max_tokens=1000,
        n=1,
        temperature=0.7,
    )
    return response
