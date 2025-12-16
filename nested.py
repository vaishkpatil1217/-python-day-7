try:
    try:
        x=int("anil")
    except ValueError:
        print("inner:value error")
except:
    print("outer block")