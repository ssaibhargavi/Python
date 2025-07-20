# The randint generates the number either 0 or 1 and if the number greater than 0.5 then heads else tails
import random
num = random.randint(0, 1)  
if num > 0.5:
  print('Heads')
else:
  print('Tails')
