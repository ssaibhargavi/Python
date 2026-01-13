# Prints number series in triangle pattern

num=0
x=int(input())
y=(int(input()))
for i in range (x,y+1):
  for j in range(1,i+1):
    num+=1
    print(num,end=" ")
  print()
