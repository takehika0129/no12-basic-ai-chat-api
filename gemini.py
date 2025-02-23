import os
import pprint
from google import genai
from google.genai import types


client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"), 
)

response = client.models.generate_content(
    model ="gemini-2.0-flash",
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful assistant. Provide responses in a clear, well-formatted style.",
        max_output_tokens=512,
    ),
    contents = "Provide some tips for effective programming.",
)

message = response.text

print("\n=== Effective Programming Tips ===\n")
pprint.pprint(message)
print("\n" + "=" * 40) 