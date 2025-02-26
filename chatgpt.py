import os
import pprint
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"), 
)

response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "system", 
            "content": "You are a helpful assistant. Provide responses in a clear, well-formatted style.",
            "role": "user",
            "content": "Give me some tips for effective programming."
        }
    ],
    max_tokens = 512
)

message = response.choices[0].message.content

print("\n=== Effective Programming Tips ===\n")
pprint.pprint(message)
print("\n" + "=" * 40) 
