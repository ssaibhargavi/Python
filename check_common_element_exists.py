# Problem: Check whether two lists share at least one common element.
# Approach: Use set intersection and evaluate if the result is non-empty.
x = [1, 3, 5, 7]
y = [2, 4, 6, 7]
if set(x) & set(y):
    print("Common elements exists")
else:
    print("No Common elements")
