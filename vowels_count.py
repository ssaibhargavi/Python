# Count vowels in an inputed string

text=input().lower()
vowels="aeiou"
count=0
for i in text:
    if i in vowels:
        count+=1
print("Count :",count)
