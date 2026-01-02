# Login Validation
# The code validates the login-based on the username and password. If both the username and password are correct it returns login Successful. If the password is incorrect it prints wrong password and if the username is incorrect it prints Invalid username

username=input()
password=input()
if username=="admin":
  if password=="1234":
    print("Login Successful")
  else:
    print("Wrong Password")
else:
  print("Invalid Username")
