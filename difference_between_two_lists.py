# Problem: Find elements that exist in the first list but not in the second list.
# Approach: Convert lists to sets and subtract the second set from the first.
p = [1, 2, 3, 4, 5]
q = [3, 4]
print(set(p)-set(q))
