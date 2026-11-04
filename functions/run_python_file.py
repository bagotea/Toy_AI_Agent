import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working, file_path))
        valid_target_dir = os.path.commonpath([abs_working, target_dir]) == abs_working
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_dir]
        if args:
            command.extend(args)
        ProcessResult = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output_str = ""
        if ProcessResult.returncode != 0:
            output_str += f"Proces exited with code {ProcessResult.returncode}\n"
        if not ProcessResult.stdout and not ProcessResult.stderr:
            output_str += f"No output produced"
        output_str += f"STDOUT: {ProcessResult.stdout}\nSTDERR: {ProcessResult.stderr}"
        return output_str
    except Exception as e:
        print(f"Error: {e}")

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "runs/executes a python program with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to python file to run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items":{
                        "type": "string",
                    },
                    "description": "optional arguments that may be used to execute the python files",
                },
            },
            "required": ["file_path"],
        },
    },
}
