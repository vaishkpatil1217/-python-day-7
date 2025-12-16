def count(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        print("Error: file not found.")

char= count("basic.py")
print("Total characters in 'file': ",char)