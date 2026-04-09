from functions.get_file_content import get_file_content

print(get_file_content("calculator", "lorem.txt"))
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat")) # should error out
print(get_file_content("calculator", "pkg/does_not_exist.py")) # should error out