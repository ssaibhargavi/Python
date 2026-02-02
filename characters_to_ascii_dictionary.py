# Problem: Create a dictionary mapping each unique character in an input string to its ASCII value.
# Approach: Use dictionary comprehension to iterate through characters and store ord() values.

text = input("Enter a string:")
ascii_map = {ch:ord(ch) for ch in text}
print(ascii_map)
