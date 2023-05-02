keyword=['True','False','None','while','for','break','continue','range','return']

user=input("Enter keywords\n")
if user in keyword:
    print(user+" " +"is a keyword")
else:
    print(user+" "+"is not a keyword")