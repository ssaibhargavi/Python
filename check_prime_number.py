# Problem: Determine whether a given number is a prime number.
# Approach: Check divisibility only up to the square root of the number and return False if any factor is found.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
num = int(input("Enter a number:"))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
