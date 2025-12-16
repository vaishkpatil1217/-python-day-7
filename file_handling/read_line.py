try:
    with open("basic.py", 'r') as file:
        for i in range(4):
          print(file.readline().strip()) 
except FileNotFoundError:
    print("Error: file not found.")
    
    
