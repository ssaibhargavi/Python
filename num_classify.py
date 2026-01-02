# Number Classification
# The code checks the numbers whether they are postitive or negative and performs the even or odd using %. It classifies the number as postitive even or odd and negative even or odd otherwise it classifies the number as Zero

number=int(input())
if number > 0:
  if number%2==0:
    print("Positive Even")
  else:
    print("Positive Odd")
elif number<0:
  if number%2==0:
    print("Negative Even")
  else:
    print("Negative Odd")
else:
  print("Zero")
