try:
    with open("basic.py",'r') as file:
        content=file.read()
        print(content)
        
    
except FileNotFoundError:
    print("file not fount")
    