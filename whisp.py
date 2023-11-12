import os
import whisper 
from openai import OpenAI

# load model 
model = whisper.load_model("medium")

# decode
result = model.transcribe("./data/sick.aac")
print(result["text"])

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "system",
            "content": "The following is a transcript of a patient call. Please summarize.",
        },
        {
            "role": "user",
            "content": result["text"]
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)