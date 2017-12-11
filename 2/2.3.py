menu = {"Borsch": 15, "Kotleta": 20, "Kasha": 10, "Chai":2}
#sort meny by value using lambda expression
sorted_x = sorted(menu.items(), key=lambda x: x[1])

print(sorted_x)