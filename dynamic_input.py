# Program that gets a dynamic number of input values.

nums=int(input())
n_sum=0
for i in range(nums):
    n=int(input())
    n_sum+=n
print(n_sum)
