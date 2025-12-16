def vote():
    try:
        age=int(input("Enter your age"))
        if age<18:
         raise Exception("You are not eligible for vote")
        else:
            print("You are eligible for vote")
    except ValueError:
        print("invalid input")
    except Exception as a:
        print(a)
vote()