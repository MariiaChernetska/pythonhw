message = input("Type word: ")
capital=sum(1 for c in message if c.isupper())
notCapital=sum(1 for c in message if c.islower())
length = len(message)
print("cap ", capital/length, "notcap ", notCapital/length)