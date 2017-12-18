class CustomParentException(Exception):

    def __init__(self, *variables):

        for var in variables:
            print(var)

        #Exception.__init__(self, 'Parent exception')

class CustomChildException1(CustomParentException):

    def __init__(self, *variables):

        for var in variables:
            print(var)

        CustomParentException.__init__(self, 'Exception is raised because probability is '+str(float(variables[0])))

class CustomChildException2(CustomParentException):

    def __init__(self, *variables):

        for var in variables:
            print(var)

        CustomParentException.__init__(self, 'Hello from child 2 exception')


def possible_fail(probability):
    if(probability>0.5):
        raise CustomChildException1(probability)


try:

   possible_fail(0.8)

except CustomChildException1 as ex:
    print(ex)

