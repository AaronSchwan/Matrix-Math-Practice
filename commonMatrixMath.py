import math
import statistics
import warnings


def zero_matrix(n: int,m:int)->list:
    """
    one_matrix(columns, rows)
    This function creates an nxm  zero matrix
    """

    #Creates and clears matrix in scope
    A = []
    A.clear()

    #Poulates matrix
    A = list(map(lambda y: list(map(lambda x: 0, range(0,n))),range(0,m)))

    #Returns matrix
    return A

def one_matrix(n: int,m:int)->list:
    """
    one_matrix(columns, rows)
    This function creates an nxm matrix full of ones
    """
    #Creates and clears matrix in scope
    A = []
    A.clear()

    #Poulates matrix
    A = list(map(lambda y: list(map(lambda x: 1, range(0,n))),range(0,m)))

    #Returns matrix
    return A


def identity_matrix(n: int)-> list:
    """
    identity_matrix(size)
    This function creates an nxn identity matrix
    """

    #Creates and clears matrix in scope
    A = []
    A.clear()

    #Poulates matrix
    A = list(map(lambda y: list(map(lambda x:1 if(y == x) else 0, range(0,n))),range(0,n)))

    #Returns matrix
    return A

def scalar_multiplication(A:list,b:float)->list:
    """
    scalar_multiplication(matrix,scalar)
    This script multiplies a scaler to every element in a python list
    """

    #Gets size of matrix
    n = len(A[0])
    m = len(A)

    #Creates and clears matrix in scope
    M = []
    M.clear()

    #Populates matrix
    M = list(map(lambda y: list(map(lambda x:A[y][x]*b, range(0,n))),range(0,m)))

    #Returns matrix
    return M

def scalar_addition(A:list,b:float)->list:
    """
    scalar_addition(matrix,scalar)
    This script adds a scaler to every element in a python list
    """

    #Gets size of matrix
    n = len(A[0])
    m = len(A)

    #Creates and clears matrix in scope
    M = []
    M.clear()

    #Populates matrix
    M = list(map(lambda y: list(map(lambda x:A[y][x]+b, range(0,n))),range(0,m)))

    #Returns matrix
    return M




def matrix_size_id_check(A:list,B:list)->list:
    """
    matrix_size(matrix,matrix)

    this script checks if two matrices are the same matrix size if they are it
    returns the size nxm if not it throws a warning "WARNING: the matrices are not the same size"
    recommended use:
    [n,m] = matrix_size(A,B)
    """

    #Gets size of matrix A
    na = len(A[0])
    ma = len(A)

    #Gets size of matrix B
    nb = len(B[0])
    mb = len(B)



    if na == nb and ma == mb:
        return na,ma

    else:
        warnings.warn("WARNING: the matrices are not the same size")





def matrix_addition(A:list,B:list)->list:
    """
    matrix_addition(matrix,matrix)

    This script takes two matrices and adds them together
    """

    #get matrix size and check for compatability
    [n,m] = matrix_size_id_check(A,B)

    #Creates and clears matrix in scope
    M = []
    M.clear()

    #Populates matrix
    M = list(map(lambda y: list(map(lambda x:A[y][x]+B[y][x], range(0,n))),range(0,m)))

    #Returns matrix
    return M



def matrix_transpose(A:list)->list:
    """
    matrix_transpose(matrix)
    this script transposes a matrix
    """

    #get matrix matrix_size
    m = len(A)
    n = len(A[0])

    #Create and clear a matrix
    M = []
    M.clear()

    #populate the matrix
    M = list(map(lambda y: list(map(lambda x:A[x][y], range(0,m))),range(0,n)))

    #return the matrix
    return M


def euclidian_dot_product(A:list,B:list)->float:
    """
    euclidian_dot_product(matrix,matrix)
    this prefroms the euclidian dot product on two vectors
    """

    #Gets size of matrix A
    ma = len(A)

    #Gets size of matrix B
    mb = len(B)



    if ma == mb:

        #find sum
        s = sum(list(map(lambda x: A[x]*B[x], range(0,ma))))
        #return sum
        return s
    else:
        warnings.warn("WARNING: the vectors are not compatible")




def matrix_multiplication(A:list,B:list)->list:
    """
    matrix_multiplication(matrix,matrix)

    This multiplies two matrices together
    """
    #Gets size of matrix A
    na = len(A)
    ma = len(A[0])

    #Gets size of matrix B
    nb = len(B)
    mb = len(B[0])


    #transposes B
    C = []
    C.clear()
    C = matrix_transpose(B)



    if ma==nb:
        #Creates and clears a matrix M
        M=[]
        M.clear()

        #populates matrix
        M = list(map(lambda y: list(map(lambda x:euclidian_dot_product(A[y],C[x]), range(0,mb))),range(0,na)))

        #returns matrix
        return M

    else:
        warnings.warn("WARNING: the matrices are not compatible")



def row_swap(A:list,r:int,R:int)->list:
    """
    This function swaps the rows of a matrix
    row_swap(matrix, row 1 , row 2)
    """
    m = len(A)

    #creates matrix
    M = []
    M.clear()

    #populates matrix
    M = list(map(lambda y:A[R] if(y==r) else( A[r] if(y==R) else A[y]),range(0,m)))

    #returns matrix
    return M


def column_swap(A:list,r:int,R:int)->list:
    """
    This function swaps the rows of a matrix
    row_swap(matrix, row 1 , row 2)
    """
    #gets matrix size
    n = len(A[0])
    m = len(A)

    #creates matrix
    M = []
    M.clear()

    #populates matrix
    M = list(map(lambda x: list(map(lambda y:A[x][R] if(y==r) else( A[x][r] if(y==R) else A[x][y]),range(0,n))),range(0,m)))

    #returns matrix
    return M

def gaussian_row_add(A:list,r:int,R:int,b:float)->list:
    """
    gaussian_row_add(matrix,row being added,row added to,constant multiple)
    this script adds one row to another returning a matrix
    """
    #get matrix size
    n = len(A[0])
    m = len(A)

    #creates and clears matrix
    M = []
    M.clear()

    #create matrix of just the row being added
    E = []
    E.clear()

    #Poulates matrix
    E = list(map(lambda y: list(map(lambda x: 0, range(0,n))) if(y != R) else(A[r]),range(0,m)))

    #Populates M

    M = matrix_addition(A,scalar_multiplication(E,b))
    #returns matrix
    return M

def gaussian_row_mult(A:list,r:int,b:float)->list:
    """
    gaussian_row_mult(matrix,row,multiplication constant)
    this script multiples one row by a constant
    """
    #get matrix size
    m = len(A)
    n = len(A[0])

    #creates and clears matrix
    M = []
    M.clear()


    #Poulates matrix
    M = list(map(lambda y: A[y] if(y != r) else list(map(lambda x: A[r][x]*b,range(0,n))),range(0,m)))

    #returns matrix
    return M


def gaussian_ref(A:list)->list:
    """
    gausian_ref(matrix)

    this script takes in a matrix and reduces it to ref using gausian operations
    """
    #create and clear matrix
    M = []
    M.clear()
    M = A

    #get matrix size
    n = len(A[0])
    m = len(A)

    #check columns decending diagonal
    for j in range(0,n):

        for i in range(j+1,m):

            if M[i][j] != 0:

                value = -M[i][j]/M[j][j]
                M = gaussian_row_add(M,j,i,value)

    #return matrix
    return M

#A = identity_matrix(4)
#B = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
#C = matrix_addition(A,B);

#print(identity_matrix(5))
#print(matrix_transpose(B))
#print(euclidian_dot_product([1,2,4,5],[2,5,4,3]))
print(gaussian_ref([[1,2,3],[3,4,5],[5,8,8]]))
#print(gaussian_row_mult(B,1,1/3))
