# Prints star triangle based on the start and end

start=int(input())
end=int(input())
for i in range(start,end):
  for j in range(1,i+1):
    print("*", end=" ")
  print()

