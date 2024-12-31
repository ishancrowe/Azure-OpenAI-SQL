from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()

deployment =  "Enter your deployement"
client = AzureOpenAI(
    api_key="Enter your api key",  # This is the default and can be omitted
    api_version="2024-05-01-preview",
    azure_endpoint = "Enter your endpoint", 
)


def get_completion_from_messages(system_message, user_message, models=deployment, temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    response = client.chat.completions.create(
        model=models,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))
