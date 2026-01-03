# Count the no.of digits in the input

num=abs(int(input("Enter a number: ")))
count=0
if num==0:
  count=1
else:
  while num>0:
    count+=1
    num=num//10
print("Count is",count)
