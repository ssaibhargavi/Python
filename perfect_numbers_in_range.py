# Problem: Print all perfect numbers within a given numeric range.
# Approach: For each number, sum its proper divisors using iteration and check if the sum equals the number.
def perfect_num(num):
    fact_sum=0
    for i in range(1,num):
        if num%i==0:
            fact_sum+=i
    if num==fact_sum:
        return True
    else:
        return False
start,end=int(input()),int(input())
for i in range(start,end+1):
    if perfect_num(i)==True:
        print(i,end=" ")
