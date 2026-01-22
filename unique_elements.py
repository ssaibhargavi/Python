# Problem: Print all numbers in a list that appear exactly once
# Approach: For each element, count its occurrences using a nested loop and collect it if the count is one
# Learning: Understood how nested loops and conditional checks can be used to identify unique elements

nums=[12,45,67,77,88,99,23,56,78,12,45,67,78]
unique=[]
for i in nums:
    if i not in unique:
        count=0
        for j in nums:
            if i==j:
                count+=1
        if count==1:
            unique.append(i)
print(unique)
