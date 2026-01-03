# Menu Program using match-case

choice=int(input())
match choice:
  case 1:
    num=int(input())
    if num%2==0:
      print("Even")
    else:
      print("Odd")
  case 2:
    num=int(input())
    if num>0:
      print("Positive")
    elif num<0:
      print("Negative")
    else:
      print("Zero")
  case 3:
    print("Exit")
  case _:
    print("Invalid")
