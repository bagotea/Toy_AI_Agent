import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import *
from call_function import available_functions, call_function
import json
import sys

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


def LLM_Call(messages_arr, tools_to_give, model = "openrouter/free"):
    return client.chat.completions.create(
        model=model,
        messages=messages_arr,
        tools=tools_to_give,
    )

def main():
    if api_key == None:
        raise RuntimeError("no api key detected")
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
    for i in range(20):
        response = LLM_Call(messages, available_functions)
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for call in message.tool_calls:
                function_args = json.loads(call.function.arguments or "{}")
                result_message = call_function(call, args.verbose)
                messages.append(result_message)
                if not result_message['content']:
                    raise Exception("ERROR: no content from tool call")
                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            return message.content
        if i == 20:
            sys.exit(1)




print(main())
