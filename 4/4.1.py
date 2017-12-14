#solution using recursion
def rec(elem, prev, index, counter):

    newprev = elem
    newelem = elem+prev

    if index == counter:
        print("Element " + str(index) + " equals " + str(prev))
        return 0

    counter+=1
    rec(newelem, newprev, index, counter)

#solution using loop
def loop(index):
    elem = 1
    prev = 0

    counter = 0
    while index != counter:
       # print(prev)
        buf = elem
        elem=elem+prev
        prev = buf
        counter+=1
    print("Element " +str(index)+" equals "+str(prev))

index = input("Enter element num ")

way = input("Use recursion - 1, loop - 2 ")
if int(way)==1:
    rec(1,0, int(index), 0)
else: loop(int(index))









