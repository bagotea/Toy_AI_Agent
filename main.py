import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import *
from call_function import available_functions
import json

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
    tools=available_functions
)

def main():
    if api_key == None:
        raise RuntimeError("no api key detected")
    if response.usage == None:
        raise RuntimeError("failed API request")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
    LLM_Response = response.choices[0].message
    if LLM_Response.tool_calls:
        for call in LLM_Response.tool_calls:
            function_args = json.loads(call.function.arguments or "{}")
            print(f"Calling function: {call.function.name}({function_args})")
    print(LLM_Response.content)
    return None


main()
