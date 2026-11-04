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
