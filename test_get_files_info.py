from functions.get_files_info import get_files_info

print(
    f"result for current directory:\n{get_files_info("calculator", ".")}\n",
    f"result for 'pkg' directory:\n{get_files_info("calculator", "pkg")}\n",
    f"result for '/bin' directory:\n{get_files_info("calculator", "/bin")}\n",
    f"result for '../' directory:\n{get_files_info("calculator", "../")}"
)
