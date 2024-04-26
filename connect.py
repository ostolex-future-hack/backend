from client import client
from text_to_speech import text_to_speech


def make_request(content: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant who helps teach English"},
            {"role": "user", "content": content}
        ]
    )
    text_to_speech(completion.choices[0].message.content)
