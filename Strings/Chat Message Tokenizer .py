#Chat Message Tokenizer — Given a chat message like "@alice can you check ticket #4521 ASAP?"
#  how do you extract all mentions (@alice) and ticket numbers (#4521)?

msg=input("enter your message:")
l=msg.split()
print(l)
mentions=[]
tokens=[]
for i in l:
    if i.startswith("@"):
        mentions.append(i)
    elif i.startswith("#"):
        tokens.append(i)

print("Mentions:",mentions)
print("Tokens:",tokens)