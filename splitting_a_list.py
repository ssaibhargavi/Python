# Separates positive and negative numbers in a list

numbers = [2, 3, -2, 5, 3, -7, 5, -9]
positive=[]
negative=[]
for i in numbers:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive numbers:",positive)
print("Negative numbers:",negative)
