import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working, file_path))
        valid_target_dir = os.path.commonpath([abs_working, target_dir]) == abs_working
        if not valid_target_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error: {e}")

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "write or overwrites a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the file to write or overwrite, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "the text to be written into the files"
                },
            },
            "required": ["file_path", "content"]
        },
    },
}
