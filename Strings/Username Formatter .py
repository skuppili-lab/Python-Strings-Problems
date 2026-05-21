# Username Formatter — A user signs up with their name as " john doe ". 
# How would you clean it up and format it as "John Doe" for display
s=input("enter your name: ")
print(s.title().strip())