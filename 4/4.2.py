def Tripple_Out(old_function):
    def new_function(*args, **kwds):
        return 3*old_function(*args, **kwds)
    return new_function


@Tripple_Out
def fun():
    return 3

print(fun())