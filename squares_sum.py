# Sum of squares from 1 to the given number

number=int(input("Enter a number:"))
total=0
for i in range(1,number+1):
  total=total+i**2
print(f"The sum of squares from 1 to {number} is {total}")
