def rec(elem, prev):
    if elem==34: return 0
    if elem==0: print(elem)
    print(elem+prev)
    newprev = elem
    newelem = elem+prev
    rec(newelem, newprev)


rec(0,1)
