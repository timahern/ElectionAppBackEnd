from openai import OpenAI
import os
from dotenv import load_dotenv

def generate_description(election_name):

    load_dotenv()
    apiKey = os.getenv("GPT_API_KEY")
    client = OpenAI(api_key = apiKey)

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": "Answer simple math questions in one short sentence."
            },
            {
                "role": "user",
                "content": "What is 2 + 2?"
            }
        ],
        #temperature=0  # deterministic answer
    )

    print(response.choices[0].message.content)

generate_description("test")