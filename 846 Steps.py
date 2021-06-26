"""
Ejercicio Uva 2
"""
import math
from sys import stdin
def main():
    cases = int(stdin.readline())
    for case in range(cases):
        a, b = map(int, stdin.readline().strip().split())
        print(op(b, a))
def op(x, y):
    n = x - y
    m = int(math.sqrt(n))
    n = n - m*m
    cont = m*2-1
    if(x-y == 1 ):
        return 1
    elif(x-y == 4):
        return 3
    elif(n <= m):
        cont += 1
    else:
        temp = m
        while(temp != 0):
            if n-temp >= 0:
                cont += 1
                n = n-m
            else:
                temp -= 1
                
    return cont

def aux(n):
    b = list(map(int, n.strip().split()))
    print(b)
                
#main()
