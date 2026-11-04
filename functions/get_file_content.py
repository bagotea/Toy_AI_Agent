from functions.config import *
import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working, file_path))
        if os.path.commonpath([abs_working, target_dir]) != abs_working:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir, 'r') as f:
            file_content = f.read(MAX_CHAR)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
        return file_content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "returns the contents of a specified file as a string",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to file to read from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["file_path"]
        },
    },
}
