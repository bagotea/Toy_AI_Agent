from functions.write_file import write_file

print(
    f"result of case lorem.txt:\n{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}\n",
    f"result of case pkg/morelorem.txt:\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}\n",
    f"result of case /tmp/temp.txt:\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}\n"
)
