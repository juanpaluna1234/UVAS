from sys import stdin
existencias = []

def main():
    global existencias
    datos = list(map(int, stdin.readline().strip().split()))
    while datos[1] != 0:
        existencias = []
        X = datos[2::]
        T = datos[0]
        print("Sums of "+str(T) +":")
        n = subSum(X,T,0,0,[])
        if n == 0:
            print("NONE")
        datos = list(map(int, stdin.readline().strip().split()))
    


def subSum(X, T, i, C, A):
    global existencias
    if C == T:
        if not(A in existencias):
            i = 0
            while i != len(A):
                if i == 0:
                    print(A[i],end = '')
                else:
                    print("+"+str(A[i]),end = '')
                i += 1
            print("")
            existencias.append(A)
        return 1
    if i >= len(X):
        return 0
    elif C < T:
        return subSum(X,T,i+1,C+X[i],A+[X[i]]) + subSum(X,T,i+1,C,A)
    else:
        return 0

main()
