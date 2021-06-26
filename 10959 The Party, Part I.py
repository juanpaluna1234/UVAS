import math
from sys import stdin, setrecursionlimit

grafo = {}
def main ():
    cases = int(stdin.readline())
    for case in range(cases):
        a, b = list(map(int, stdin.readline().strip().split()))
        fiesta(a , b)


def fiesta (per, par):
    global grafo
    cases = par
    grafo = crearGrafo(per)
    for case in range(cases):
        a, b = list(map(str, stdin.readline().strip().split()))
        temp1 = grafo.get(a)
        temp1.append(b)
        temp2 = grafo.get(b)
        temp2.append(a)
        grafo.update({a : temp1})
        grafo.update({b : temp2})
    busqueda(grafo, per)


def crearGrafo(n):
    aux = {"0" : []}
    i = 1
    while n > i:
        aux.update({str(i) : []})
        i = i+1
    return aux

def busqueda(g, n):
    per = crearGrafo(n)
    recorridos = ['0']
    