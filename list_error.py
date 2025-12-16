def index():
    try:
        list=[1,2,3,4,5,6]
        print(list[6])
    except IndexError:
        print("wrong indexing...")
index()