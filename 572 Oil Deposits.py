import math
from sys import stdin
from collections import deque

matrix = []
contador = 0
m = 1
n = 1
def main ():
    global n, m, contador
    while m != 0 and n != 0:
        m, n = list(map(int, stdin.readline().strip().split()))
        if m != 0 and n != 0:
            oilDep()
        contador = 0

def oilDep ():
    global n, m
    global matrix
    cases = m
    plot = []
    for case in range(cases):
        aux = stdin.readline().strip()
        plot.append(aux)
    num = 0
    i = 0
    j = 0
    new = []
    while i < m:
        new.append([])
        j = 0;
        while j < n:
            if plot[i][j] == '@':
                new[i].append(num)
                num += 1
            else:
                new[i].append(-1)
            j += 1
        i += 1
    matrix = new
    if m == 1 or n == 1:
        casoEspecial()
    else:
        crearGrafo()
    print (contador)


def crearGrafo():
    global n, m
    global matrix, contador
    i = 0
    while i < m:
        j = 0
        while j < n:
            if matrix[i][j]!= -1:
                busqueda(i, j)
                contador += 1
            j += 1
        i += 1
            
def busqueda(i,j):
        global n, m
        global matrix
        matrix[i][j] = -1
        if i == 0:
            if j == 0:
                if matrix[i][j+1]!= -1:
                    busqueda(i,j+1)
                if matrix[i+1][j]!= -1:
                    busqueda(i+1, j)
                if matrix[i+1][j+1]!= -1:
                    busqueda(i+1, j+1)
            elif j == n-1:
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
                if matrix[i+1][j-1]!= -1:
                    busqueda(i+1, j-1)
                if matrix[i+1][j]!= -1:
                    busqueda(i+1, j)
            else:
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
                if matrix[i][j+1]!= -1:
                    busqueda(i, j+1)
                if matrix[i+1][j-1]!= -1:
                    busqueda(i+1, j-1)
                if matrix[i+1][j]!= -1:
                    busqueda(i+1, j)
                if matrix[i+1][j+1]!= -1:
                    busqueda(i+1, j+1)
        elif i == m-1:
            if j == 0:
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i-1][j+1]!= -1:
                    busqueda(i-1, j+1)
                if matrix[i][j+1]!= -1:
                    busqueda(i, j+1)
            elif j == n-1:
                if matrix[i-1][j-1]!= -1:
                    busqueda(i-1, j-1)
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
            else:
                if matrix[i-1][j-1]!= -1:
                    busqueda(i-1, j-1)
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i-1][j+1]!= -1:
                    busqueda(i-1, j+1)
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
                if matrix[i][j+1]!= -1:
                    busqueda(i, j+1)
        else:
            if j == 0:
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i-1][j+1]!= -1:
                    busqueda(i-1, j+1)
                if matrix[i][j+1]!= -1:
                    busqueda(i, j+1)
                if matrix[i+1][j] != -1:
                    busqueda(i+1, j)
                if matrix[i+1][j+1]!= -1:
                    busqueda(i+1, j+1)
            elif j == n-1:
                if matrix[i-1][j-1]!= -1:
                    busqueda(i-1, j-1)
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
                if matrix[i+1][j-1]!= -1:
                    busqueda(i+1, j-1)
                if matrix[i+1][j]!= -1:
                    busqueda(i+1, j)
            else:
                if matrix[i-1][j-1]!= -1:
                    busqueda(i-1, j-1)
                if matrix[i-1][j]!= -1:
                    busqueda(i-1, j)
                if matrix[i-1][j+1]!= -1:
                    busqueda(i-1, j+1)
                if matrix[i][j-1]!= -1:
                    busqueda(i, j-1)
                if matrix[i][j+1]!= -1:
                    busqueda(i, j+1)
                if matrix[i+1][j-1]!= -1:
                    busqueda(i+1, j-1)
                if matrix[i+1][j]!= -1:
                    busqueda(i+1, j)
                if matrix[i+1][j+1]!= -1:
                    busqueda(i+1, j+1)
def casoEspecial():
    global matrix, contador
    if m == 1 and n == 1:
        if matrix[0][0] != -1:
            contador += 1
    elif(m == 1):
        j = 0
        concatenado = False
        while j < n:
            if matrix[0][j] == -1:
                if concatenado:
                   concatenado = False 
            else:
                if not concatenado:
                    contador += 1
                    concatenado = True
            j += 1
    else:
        i = 0
        concatenado = False
        while i < m:
            if matrix[i][0] == -1:
                if concatenado:
                   concatenado = False 
            else:
                if not concatenado:
                    contador += 1
                    concatenado = True
            i += 1


main()

    
