from functions.run_python_file import run_python_file

print(
    f"Result calculator main: \n{run_python_file("calculator", "main.py")}\n",
    f"Result calculator 3 + 5: \n{run_python_file("calculator", "main.py", ["3 + 5"])}\n",
    f"Result calculator tests: \n{run_python_file("calculator", "tests.py")}\n",
    f"Result calculator outofscope: \n{run_python_file("calculator", "../main.py")}\n",
    f"Result calculator nonexistent: \n{run_python_file("calculator", "nonexistent.py")}\n",
    f"Result calculator nonexecutable: \n{run_python_file("calculator", "lorem.txt")}\n"
)
