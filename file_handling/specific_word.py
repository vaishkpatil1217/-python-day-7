import re
count=0
def count1(filename,word):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content) 
            return words.count(word)
    except FileNotFoundError:
        print("Error: file not found.")
        return 0

filename="basic.py"
word='result'

word1= count1(filename,word)
print("the words",word,"occurs",word1,"times")