import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.environ['openAI_key'],
)

prompt = input("Write your prompt: ")
print("waiting for chatGPT's responce...")
print("")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

gpt_answer = chat_completion.choices[0].message.content
print(f"GPT's answer: {gpt_answer}")
