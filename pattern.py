# Prints stars based on the input x and y

x=int(input())
y=int(input())
for i in range(1,x):
  for j in range(1,y):
    print("*", end=" ")
  print()
