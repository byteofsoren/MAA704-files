import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def get_rowMean(A, setlatex=0):
    ''' calculates mean for each row in a sympy matrx
        A is the matrix.
        iffe setlatex != 0 then a LaTeX output is generated with setLatex as a variablename
        RETURNS a sympy matrix with mean of each row
    '''
    #print("got the matrix\n" + str(A))
    temp = A.tolist()
    rows = len(temp)
    m = []
    for i in np.arange(0,rows):
        m.append([np.mean(np.array(temp[i]).astype(np.float))])
    mean = Matrix(m)
    if setlatex != 0:
        print("\\begin{equation}\n" + str(setlatex) + "=")
        pMatrix(mean, setlatex=1)
        print("\\end{equaiton}")
    return mean

def removemean(A, frommean=0,setlatex=0):
    ''' Removes the mean of an matrix
        A = Matrix with 2 rows x,y
        return A - mean
    '''
    if type(frommean)!=type(A):
#        mean = Matrix([np.mean(np.array(A.tolist()[0]).astype(np.float)),
#              np.mean(np.array(A.tolist()[1]).astype(np.float))])
#        temp = A.tolist()
#        rows = len(temp)
#        m = []
#        for i in np.arange(0,rows):
#            m.append([np.mean(np.array(temp[i]).astype(np.float))])
#        mean = Matrix(m)
         mean = get_rowMean(A)
    else: #mean is a matrix
#        mean = Matrix([np.mean(np.array(frommean.tolist()[0]).astype(np.float)),
#              np.mean(np.array(frommean.tolist()[1]).astype(np.float))])
        temp = frommean.tolist()
        rows = len(temp)
        m = []
        for i in np.arange(0,rows):
            m.append([np.mean(np.array(temp[i]).astype(np.float))])
        mean = Matrix(m)
    #print("mean=\n" + str(mean))
    data = A
    # remove mean form data.
    length = len(data.tolist()[0])
    temp = []
#    for i in np.arange(0,length):
#        x = data.tolist()[0][i] - mean.tolist()[0][0]
#        y = data.tolist()[1][i] - mean.tolist()[1][0]
#        #print("x=" + str(x) + " y=" + str(y))
#        temp.append([x,y])
#    temp = Matrix(temp)
    cols=len(data.tolist()[0])
    col = []
    for i in np.arange(0,cols):
        r = []
        for j in np.arange(0,rows):
            #print("i=" + str(i) + " j=" + str(j))
            t = data.tolist()[j][i] - mean.tolist()[j][0]
            #print(t)
            r.append(t)
        col.append(r)
    temp = Matrix(col)
    return temp

def covariance(A, setlatex=0):
    ''' Calculates the covariance of a matrix A.
        A = Matrix with n rows
        setLatex = 0 is a condition to turn on latex printing of each math stepp.
        returns M=covariance matrix
    '''
    #from sympy import *
    #print("got the matrix\n" + str(A))
    temp = A.tolist()
    rows = len(temp)
    m = []
    for i in np.arange(0,rows):
        m.append([np.mean(np.array(temp[i]).astype(np.float))])
    mean = Matrix(m)
#    mean = Matrix([np.mean(np.array(A.tolist()[0]).astype(np.float)),
#          np.mean(np.array(A.tolist()[1]).astype(np.float))])
    #print("mean=\n" + str(mean))
    data = A
    # remove mean form data.
#    length = len(data.tolist()[0])
#    temp = []
#    for i in np.arange(0,length):
#        x = data.tolist()[0][i] - mean.tolist()[0][0]
#        y = data.tolist()[1][i] - mean.tolist()[1][0]
#        #print("x=" + str(x) + " y=" + str(y))
#        temp.append([x,y])
#   temp = Matrix(temp)
    cols=len(data.tolist()[0])
    col = []
    for i in np.arange(0,cols):
        r = []
        for j in np.arange(0,rows):
            #print("i=" + str(i) + " j=" + str(j))
            t = data.tolist()[j][i] - mean.tolist()[j][0]
            #print(t)
            r.append(t)
        col.append(r)
    temp = Matrix(col)
    #pMatrix(temp)
    #print("temp=" + str(temp))
    length = cols
    cov = 1/(length -1 )*transpose(temp)*temp
    #print("cov=\n" + str(cov))
    if setlatex != 0:
        print("\\begin{equation}")
        print(str(setlatex) + "=" + latex(A) + " \\Rightarrow")
        print("\\overline{x}^T=")
        #print(str(latex(mean)))
        pMatrix(mean, setlatex="\\overline{x}^T_" + str(setlatex))
        print("\\end{equation}")
        print("\\begin{equation}")
        #print("\\text{norm}=" + str(latex(temp)))
        print("\\text{norm}=")
        pMatrix(temp, setlatex=1)
        print("\\end{equation}")
        print("\\begin{equation}")
        print("M:=\\frac{1}{D-1}*\\text{norm}^T*\\text{norm}")
        print("\\end{equation}")
        print("\\begin{equation}")
        #print("m=" + str(1/(length -1)) + str(latex(transpose(temp))) + "*" + str(latex(temp)) + "=" + str(latex(cov)))
        print("m=" + str(1/(length -1)))
        pMatrix(transpose(temp), setlatex=1)
        print("*")
        pMatrix(temp, setlatex=1)
        print("=")
        pMatrix(cov, setlatex=1)
        print("\\end{equation}")
    return cov

def pMatrix(m, decimals=3, setlatex=0):
    ''' Prints matrixes that are rounded in each cell to n decimals.
        m = sympy matrix
        decimals = nr of decimals that is needed
        pirts a rounded latex matrix
        return nothing
    '''
    temp = np.array(m.tolist()).astype(np.float)
    tr = temp.round(decimals)
    if setlatex == 0:
        print(str(tr))
    else:
        mx = Matrix(tr)
        if setlatex != 1:
            print(str(setlatex) + "=")
        print(str(latex(mx)))
    pass

# test cases.
if __name__ == "__main__":
    c1 = Matrix([[1,0],
             [1,1],
             [2,2],
             [2,3]])
    pMatrix(c1, setlatex=1, decimals=3)
    A = Matrix([[-4,2],
              [-3,1],
              [-1,0],
              [1,0] ,
              [3,-1],
              [4,-2]])
    covariance_of_A= Matrix([[10.4, -4.4],
                            [-4.4, 2.0]])
    M = covariance(transpose(A), setlatex=1)
    print("M=\n" + str(M) + "\ncovariance_of_A=\n" + str(covariance_of_A))
