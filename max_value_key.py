# Problem: Identify the key associated with the highest value in a dictionary.
# Approach: Iterate through dictionary items while tracking the maximum value and its corresponding key.

marks = {"A":45, "B":78, "C":90, "D":34}
max_value=0
max_key=None
for key,value in marks.items():
    if value > max_value:
        max_value = value
        max_key=key
print(max_key)
