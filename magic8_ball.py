# The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 
# It respond to any Yes or No questions with a different answer each time it executes.

import random
qn=input("Enter a question: ")
num=random.randint(1,9)
if(num==1):
  ans="Yes - definitely"
elif(num==2):
  ans="It is decidedly so"
elif(num==3):
  ans="Without a doubt"
elif(num==4):
  ans="Reply hazy, try again"
elif(num==5):
  ans="Ask again later"
elif(num==6):
  ans="Better not tell you now"
elif(num==7):
  ans="My sources say no"
elif (num==8):
  ans="Outlook not so good.','Very doubtful"
else:
  ans="Error"
print("Magic 8 ball: ",ans)
