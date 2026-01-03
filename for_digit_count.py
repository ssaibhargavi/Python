# Counts the no.of digits using for loop

num =input().lstrip('-')
if num == 0:
    count = 1
else:
  count=0
  for i in num:
    if i.isdigit():
      count+=1
print("Count is", count)
