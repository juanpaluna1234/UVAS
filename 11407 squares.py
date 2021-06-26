from sys import stdin
import math
cuad = [-1 for _ in range(10000)]
def main():
    global cuad
    casos = int(stdin.readline().strip())
    calculo()
    while casos:
        caso = int(stdin.readline().strip())
        print(cuad[caso-1])
        casos -= 1

def squares(n,m):
    global cuad
    i = 1
    while i < math.sqrt(n):
        cuad[m] = min(cuad[m], 1 + cuad[m - i**2])
        i += 1

def calculo():
    global cuad
    i = 1
    while i <= 10000:
        aux = math.sqrt(i)
        if aux == int(aux):
            cuad[i-1]=1
        else:
            cuad[i-1] = i
            squares(i,i-1)
        i += 1
main()
    
