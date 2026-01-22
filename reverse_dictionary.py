# Problem: Reverse a dictionary by grouping keys that share the same value
# Approach: Iterate through each key–value pair in the dictionary, use a new dictionary where values become keys and store the original keys in a list, initializing the list when the value is encountered for the first time
# Learning: Learned how to handle duplicate values when reversing dictionaries by aggregating keys into lists, and how conditional initialization prevents KeyErrors while keeping the solution efficient and readable

data = {"a": 1, "b": 2, "c": 1}
reversed_data = {}
for key, value in data.items():
    if value not in reversed_data:
        reversed_data[value] = []
    reversed_data[value].append(key)
print(reversed_data)
