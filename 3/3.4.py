numb = input("enter number ")
if numb[0] != "-":
    print(numb[::-1])
else:
    print("-"+numb[1:len(numb)][::-1])