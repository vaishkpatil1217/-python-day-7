def cube(no):
    if not isinstance(no,int):
        pass
    return no*no*no
try:
    print(cube(2))
    print(cube("vaish")) 
except TypeError:
    print("enter only intergers")
    
