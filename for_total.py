# prints total of number using for loop

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
