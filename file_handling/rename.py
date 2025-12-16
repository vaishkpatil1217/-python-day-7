import os

def rename(old, new):
    if not os.path.exists(old):
        print("Error: File ",old," not found.")
    try:
        os.rename(old, new)
        print("Successfully renamed",old,"to",new,".")
    except Exception as e:
        print("An error occurred while renaming: ",e)

old = "read.py"
new = "basic.py"
rename(old,new)