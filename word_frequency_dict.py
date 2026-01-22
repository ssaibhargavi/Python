# Problem: Count the frequency of each word in a sentence
# Approach: Split the sentence into words, iterate through them, and use a dictionary to keep track of how many times each word appears—incrementing the count if the word already exists, otherwise initializing it to 1
# Learning: Learned how dictionaries make frequency counting straightforward and efficient, and why this single-pass approach is far superior to nested loops for text analysis tasks

sentence = "python is easy and python is powerful"
word_freq={}
for i in sentence.split(' '):
    if i in word_freq:
        word_freq[i]+=1
    else:
        word_freq[i]=1
print(word_freq)
