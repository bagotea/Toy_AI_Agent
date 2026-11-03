from functions.get_file_content import get_file_content


def test(test_file: str):
    if test_file == "lorem.txt":
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        return
    print(get_file_content("calculator", test_file))

test("lorem.txt")
test("main.py")
test("pkg/calculator.py")
test("/bin/cat")
test("pkg/does_not_exist.py")
