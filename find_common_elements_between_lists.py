# Problem: Find elements that are common between two lists.
# Approach: Convert both lists to sets and compute their intersection.

a = [10, 20, 30, 40]
b = [30, 40, 50, 60]
print(set(a)&set(b))
