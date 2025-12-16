def value():
    try:
        x= int(input("Input the first number: "))
        y= int(input("Input the second number: "))
        print("devide", x/y)
    except ValueError:
        print("value error")
    else:
        print("code finished")
    finally:
        print("thank you")
value()