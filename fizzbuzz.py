# the code prints FizzBuzz if it the multiple of 3 and 5, prints Fizz if the number is only the multiple of 3, it prints buzz if the number is the multiple of 5 and it prints the given number if the above conditions failec
a=int(input())
if a%3==0 and a%5==0:
  print("FizzBuzz")
elif a%3==0:
  print("Fizz")
elif a%5==0:
  print("Buzz")
else:
  print(a)
