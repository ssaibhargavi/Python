# Problem: Count the frequency of each character in a given string.
# Approach: Iterate through the string and increment counts in a dictionary using get().
def char_freq(text):
    freq = {}
    for ch in text.lower():
        freq[ch] = freq.get(ch, 0) + 1
    return freq
text = input("Enter text: ")
print(char_freq(text))
