# Factorial of a given number

n=int(input())
fact=1
if n==0 or n==1:
    fact=1
else:
    for i in range(1,n+1):
        fact*=i
print("Factorial of {} is {}".format(n, fact))
