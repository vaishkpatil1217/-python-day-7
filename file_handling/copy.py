def copy_file(source, destination):
    try:
        with open(source, 'r') as source_file:
            content = source_file.read()
        with open(destination, 'w') as destination_file:
            destination_file.write(content)
        print("Successfully copied ",source," to",destination,".")
    except FileNotFoundError:
        print("Error: Source file ",source," not found.")
    except Exception as e:
        print(f"An error occurred:",e)

source_file = "read.py"
destination_file = "copied_sample.txt"
copy_file(source_file, destination_file)