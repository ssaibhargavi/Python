# Prints reverse number triangle based on the input

start=int(input())
end=int(input())
for i in range(start,end,-1):
  for j in range(1,i+1):
    print(j, end=" ")
  print()
