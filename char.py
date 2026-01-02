# Checks whether a character is an alphabet or digit or a special character.

char=input()
if char>='a' and char<='z' or char>='A' and char<='Z':
  print("Alphabet")
elif char>='0' and char<='9':
  print("Digit")
else:
  print("Special character")
