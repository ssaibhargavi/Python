# Sum of digits in a number using while loop

num = int(input())
d_sum = 0
if num == 0:
    d_sum = 0
else:
    temp = abs(num)
    while temp > 0:
        d_sum += temp % 10
        temp //= 10
print("Sum of digits:",d_sum)
