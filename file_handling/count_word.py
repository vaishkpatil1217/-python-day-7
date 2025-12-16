import re
def count(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\W+', content) 
            return len(words)
    except FileNotFoundError:
        print("Error: file not found.")

word= count("basic.py")
print(f"Total words in 'file': ",word)