def value1(ac):
    while True:
        try:
            value = float(input(ac))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")

n1 = value1("Input the first number: ")
n2 = value1("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)
