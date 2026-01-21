# Finds the second largest number in a list

numbers = [2, 3, 2, 15, 3, 7, 5]
largest=float('-inf')
second_largest=float('-inf')
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif largest>i>second_largest:
        second_largest=i
print("Largest:",largest)
print("Second largest:",second_largest)
