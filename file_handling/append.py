filename = "extra.txt"
append = "This is an appended line."

try:
    with open(filename, 'a') as file:
        file.write("\n" + append)
    print("Successfully appended ",append," to ",filename,".")
except FileNotFoundError:
    print("Error:file not found.")
except Exception as e:
    print("An error occurred:",e)