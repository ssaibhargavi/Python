# Program that finds all pairs of numbers that multiply to give n using numbers from 1 to n (inclusive).

n = int(input())
print(f"Multiples of {n}:")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j==n:
            print(i,j)
