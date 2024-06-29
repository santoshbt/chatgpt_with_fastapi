from openai import OpenAI
import os

os.load_dot_env

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator,
                        Generate multi paragraph rich text product description with emojis from
                        the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})

    completion = client.chat.completions.create(
       messages=messages,
       model="gpt-3.5-turbo"
    )

    reply = completion.choices[0].message.content
    print(reply)
    return reply
