def value(ac):
    try:
        value = int(input(ac))
        return value
    except ValueError:
        print("Error: Invalid input, input a valid integer.")


n = value("Input an integer: ")
print("Input value:", n)
