from openai import OpenAI

client = OpenAI(
    api_key="12011d66443b471d8d5d7d91cc5320ea",
    base_url="https://api.aimlapi.com",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Hi there",
        }
    ]
)

message = response.choices[0].message.content
print(f"Assistant: {message}")