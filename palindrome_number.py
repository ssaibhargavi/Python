# Checks whether a number is palindrome number or not

original_number=int(input("Enter a number:"))
reversed_number=0
temp_number=original_number
while original_number>0:
    digit=original_number%10
    reversed_number=reversed_number*10+digit
    original_number=original_number//10
if temp_number==reversed_number:
    print(f"{temp_number} is a palindrome number")
else:
    print(f"{temp_number} is not a palindrome number")
