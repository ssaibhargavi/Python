# The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 
# It respond to any Yes or No questions with a different answer each time it executes.

import random
qn=input("Enter a question: ")
ans=random.randint(1,8)
if(ans==1):print('Yes - definitely.')
elif(ans==2):print('It is decidedly so.')
elif(ans==3):print('Without a doubt.')
elif(ans==4):print('Reply hazy, try again.')
elif(ans==5):print('Ask again later.')
elif(ans==6):print('Better not tell you now.')
elif(ans==7):print('My sources say no.')
else:print('Outlook not so good.','Very doubtful.')
