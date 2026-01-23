# Problem: Group a list of integers into even and odd numbers using a dictionary of lists.
# Approach: Iterate through the list and append each number to the "even" or "odd" key based on modulo check.

numbers=[2,5,98,3,67,89,24,75,12,90,32,56]
group_numbers={"even":[],"odd":[]}
for i in numbers:
    if i%2==0:
        group_numbers["even"].append(i)
    else:
        group_numbers["odd"].append(i)
print(group_numbers)
