#Password Strength Checker
#Input a password and return a strength report:

password=input("Enter your password: ")
strenght=0
if len(password)>=8: #checks the length of the password
   strenght=strenght+1

for i in password:
    if i.isupper(): #checks for any uppercase letters in the password
        strenght=strenght+1
    if i.isdigit(): #checks for any digits in the password
        strenght=strenght+1
    if not i.isalnum(): #checks for any special characters in the password
        strenght=strenght+1
if strenght>=6: 
    print("Strong password")
elif strenght>=3 and strenght<=5:
    print("Medium password")
else:
    print("Weak password")