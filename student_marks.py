# the code checks the student marks and prints their grade. using the if-else and comparision operators between the marks it prints the grades.

marks=int(input())
if marks >= 90:
  print("A")
elif marks >=75 and marks <= 89:
  print("B")
elif marks>=50 and marks <= 74:
  print("C")
elif marks < 50 and marks >=0 :
  print("Fail")
else:
  print("Negative marks") 
