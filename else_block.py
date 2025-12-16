def divide():
    try:
        x= int(input("Input the first number: "))
        y= int(input("Input the second number: "))
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("zero division error")
    else:
        print("code finished")
divide()