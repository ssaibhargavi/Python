# Finds frequency of each element in a list

numbers = [2, 3, 2, 5, 3, 7, 5]
seen=[]
for i in numbers:
    if i not in seen:
        count=0
        for j in numbers:
            if i==j:
                count+=1
        print(f"{i} appears {count} times")
        seen.append(i)
