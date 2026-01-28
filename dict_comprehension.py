# character frequency in a string using dictionary comprehension

string=input("Enter a string:")
dict1={i:string.count(i) for i in string}
print(dict1)
