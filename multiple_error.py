def value():
 try:
     x=int(input("enter first no"))
     y=int(input("enter second no"))
     print("devide of x and y is ",x/y)
 except ValueError:
     print("value error")
 except ZeroDivisionError:
     print("value error")
    
value()

        