import random
#list result creation
numbers = list()

#filling list with rnd numbers


numbers = [random.randint(1, 100) for i in range(10)]
#print rnd list
print(numbers)

print("-------")
#print sorted list
numbers.sort()
print(numbers)