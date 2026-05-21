#E mail Validator — Given an email like "user@example.com",
# how do you check if it contains @ and ends with .com?
e_mail=input("enter your email:")
print("VALID Email" if e_mail.find("@")!=-1 and e_mail.endswith(".com") else "INVALID Email")
 