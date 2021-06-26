from sys import stdin
import math

def main():
    datos = list(map(int, stdin.readline().strip().split()))
    while datos:
        i = 0
        lista = []
        for i in range(datos[0]):
            dato = list(map(int, stdin.readline().strip().split()))
            lista.append(dato)
        aux = intervalo(lista,datos)
        print(grass(0,datos[1],aux))
        datos = list(map(int, stdin.readline().strip().split()))

def grass(L,H,a):
    a.sort()
    ans, low, n, ok, N = 0, L, 0, True, len(a)
    while ok and low < H and n != N:
        ok = a[n][0] <= low
        best, n = n, n+1
        while ok and n != N and a[n][0] <= low:
            if a[n][1] > a[best][1]:
                best = n
            n += 1
        ans += 1
        low = a[best][1]
    ok = ok and low >= H
    if ok == False:
        ans = -1
    return ans

def intervalo(a,b):
    lista = []
    for elem in a:
        temp = pow(elem[1],2) - pow(b[2]/2,2)
        if temp >= 0:
            val = math.sqrt(temp)
            low = elem[0]-val
            high = val+elem[0]
            lista.append([low,high])
    return lista

main()
    
