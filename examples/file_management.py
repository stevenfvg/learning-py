# This script demonstrates how to create a .txt file in Python using the open() function.

# File name and mode
file_name = "example.txt"
mode = "w"  # 'w' mode means write mode, which will create a new file or overwrite an existing one

# Content to write into the file
content = """
This is an example of writing text to a file using the open() function in Python.
You can add multiple lines of text, and each line will be written to the file.
Python makes file handling easy and intuitive.
"""

# Open the file in write mode
with open(file_name, mode) as file:
    # Writing the content to the file
    file.write(content)
    # No need to close the file manually; the 'with' statement handles it automatically

# Confirmation message
print(f"File '{file_name}' has been created and written successfully.")

# You can now find 'example.txt' in the same directory as this script.
# The file will contain the content written above.
