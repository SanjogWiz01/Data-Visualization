from ollama import Client

client = Client()
response = client.chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)

print(response['message']['content'])
