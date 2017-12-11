n = input("Enter N   ")
#creates triangular matrix using N
def create_matrix(size):
    #result two dimensional list
    res = list()

    #creating matrix rows from 1 to N, from 1 to N-1, from 1 to N-2...
    for i in range(size+1, 1, -1):
        #append row to result matrix
        res.append(list(range(1, i)))
    return res

#try parse matrix size to int
try: 
    
    matrixSize = int(n)
    resMatrix = create_matrix(matrixSize)
    #pring result matriz
    for line in resMatrix:
        print(line, end="\n")
#parsing exception
except ValueError: print("Enter valid num")


