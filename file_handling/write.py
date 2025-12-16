
try:
    with open("extra.txt", 'w') as file:
        file.write("Hello User")
except Exception as e:
    print("An error occurred:",e)