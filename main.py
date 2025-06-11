import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


user_prompt = sys.argv[1:]


if len(user_prompt) == 0:
    print("You need to input a prompt to get this working!")
    sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt[0])]),
]


response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

prompt_token = response.usage_metadata.prompt_token_count
response_token = response.usage_metadata.candidates_token_count


if len(user_prompt) == 2 and user_prompt[1] == "--verbose":
    print("User prompt:", user_prompt[0] )
    print("Prompt tokens:", prompt_token )
    print("Response tokens:", response_token )
else: 
    print("User prompt:")
    print("Prompt tokens:")
    print("Response tokens:")