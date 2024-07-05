import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
            "content": "You are an experienced software developer and engineer specializing in Desktop Development (Windows Desktop Apps) for professional, scalable, and long-term applications and support."},
        {"role": "user", "content": "What is the best Windows framework or technology to use for desktop Windows development?"}
    ],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
