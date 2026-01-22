# Problem: Count the frequency of each character in a string
# Approach: Iterate through each character in the string, use a dictionary to track counts, increment the value if the character already exists, otherwise initialize it to 1
# Learning: Learned how dictionaries efficiently store and update frequency counts in a single pass, avoiding the unnecessary overhead of nested loops and making the solution both cleaner and more scalable

text = "programming"
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
