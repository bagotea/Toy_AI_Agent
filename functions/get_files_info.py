import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working, directory))
        valid_target_dir = os.path.commonpath([abs_working, target_dir]) == abs_working
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        files = os.listdir(target_dir)
        files_info = ""
        for file in files:
            file_dir = os.path.join(target_dir, file)
            files_info += f"-{file}: file_size={os.path.getsize(file_dir)} bytes, is_dir={os.path.isdir(file_dir)}\n"
        return files_info
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
