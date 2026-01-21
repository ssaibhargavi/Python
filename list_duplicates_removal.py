# Remove duplicates (preserve order)

numbers = [2, 3, 2, 5, 3, 7, 5]
numbers_list=[]
for i in numbers:
    if i not in numbers_list:
        numbers_list.append(i)
print(numbers_list)
