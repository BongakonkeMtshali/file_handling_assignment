# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is the second line.\n")
        file.write("12345\n")
    print("File created and written successfully.")
except IOError as e:
    print(f"An error occurred while creating or writing to the file: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appended line 1.\n")
        file.write("Appended line 2.\n")
        file.write("Appended line 3.\n")
    print("Additional lines appended successfully.")
except IOError as e:
    print(f"An error occurred while appending to the file: {e}")

# Final Reading and Display to confirm appending
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nUpdated file content:")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
