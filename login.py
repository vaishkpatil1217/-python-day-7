try:
    username=input("Enter username: ")
    password=input("Enter password: ")
    
    if username!="admin"or password!="1234":
        raise Exception("Invalid login")
    print("login successfull")
except Exception as a:
    print(a)