# Leap year
# The code tells whether a year is leap year or not. A leap year is divisible by 4 or 400 but not divisible by 100.

year=int(input())
if year%4==0 or  year%400==0 and year%100!=0:
  print("%d is leap year"%(year))
else:
  print("%d is not leap year"%(year))
