# Simple Calculator program using match-case

a=int(input())
b=int(input())
operator=input().strip()
match operator:
  case '+':
    print(a+b)
  case '-':
    print(a-b)
  case '*':
    print(a*b)
  case '/':
    if b!=0:
      print(a/b)
    else:
      print("Divsion by zero is not possible")
  case _:
    print("Invalid")
