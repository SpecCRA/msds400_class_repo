import numpy as np
from numpy import *
from numpy.linalg import inv
import sys

def solveForX(A,B):
    try:
        Ainv=inv(np.matrix(A))
        X=np.matmul(Ainv,B)
        print('X: The result of inverse(A)*B =')
        print(X)
        return
    except np.linalg.LinAlgError as e:
         if 'Singular matrix' in str(e):
            print('Error: A is a singular matrix')
    except np.ValueError as e:
           print('Error: matrix multiplication value error')
    else:
        raise

# Enter the dimensions and elements of matrix A
numRowsA = int(input("Enter number of rows in matrix A: "))
numColsA = int(input("Enter number of columns in matrix A: "))
print('Enter the {}X{} matrix A:'.format(numRowsA, numColsA))
A=np.empty(shape=(numRowsA, numColsA),dtype=float)
for i in range(numRowsA):
    for j in range(numColsA):
        A[i][j]=float(input("Enter the element: "))
print('A:')
print(A)

if numRowsA != numColsA:
    print ('Error: A is not a square matrix!')
    sys.exit()


# Enter the dimensions and elements of matrix B
numRowsB = int(input("Enter number of rows in matrix B: "))
numColsB = int(input("Enter number of columns in matrix B: "))
print('Enter the {}X{} matrix B:'.format(numRowsB, numColsB))
B=np.empty(shape=(numRowsB, numColsB),dtype=float)
for i in range(numRowsB):
    for j in range(numColsB):
        B[i][j]=float(input("Enter the element: "))
print('B:')
print(B)

if numColsA != numRowsB:
    print ('Error: matrices inv(A) and B cannot be multiplied!')
    sys.exit()

# invoke the solveForX function to compute the inverse of A
# and to multiply the result with B
X=solveForX(A,B)