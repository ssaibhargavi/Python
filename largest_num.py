# Finds largest digit in a number

number=int(input())
largest_digit=0
while number>0:
    digit=number%10
    if digit>largest_digit:
        largest_digit=digit
    number//=10
print("Largest digit:",largest_digit)
