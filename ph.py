# Checking the ph levels based on the input

ph=int(input("Enter value between 1 to 14: "))
if(ph<7):
  print("Acidic")
elif(ph>7):
  print("Basic")
else:
  print("Neutral")
