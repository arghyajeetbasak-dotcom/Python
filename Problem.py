import os

# Get the current working directory
directory = os.getcwd()

# Print the directory path
print(f"Contents of the directory: {directory}")

# List and print the contents
try:
    contents = os.listdir(directory)
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")