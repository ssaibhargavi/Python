# Prints number triangle based on input

start=int(input())
end=int(input())
for i in range(start,end):
  for j in range(1,i+1):
    print(j, end=" ")
  print()
