import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import *

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="MyAIAgent")
parser.add_argument("prompt", type=str, help="Your Prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

def main():
    if api_key == None:
        raise RuntimeError("no api key detected")
    if response.usage == None:
        raise RuntimeError("failed API request")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)
    return None


main()
