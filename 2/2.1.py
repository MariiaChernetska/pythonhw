import random
#list result creation
numbers = list()

#filling list with rnd numbers
for i in range(10):
    numbers.append(random.randint(1, 100))

#print rnd list
print(numbers)

print("-------")
#print sorted list
numbers.sort()
print(numbers)