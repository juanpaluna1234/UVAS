import math
from sys import stdin
from collections import deque

def main ():
    x,y,z,case = 1, 1, 1, 0
    while x!= 0 or y != 0 or z != 0:
        case += 1
        x, y, z = list(map(int, stdin.readline().strip().split()))
        if x != 0 or y != 0 or z != 0:
            val = list(map(int, stdin.readline().strip().split()))
            busqueda(x, y, z, val, case)
def busqueda (x, y, z, val, case):
    visited, queue, calculado = [False for _ in range(10000)], deque(), [0 for _ in range(10000)]
    visited[x] = True; queue.append(x); calculado[x] = 1
    while len(queue) > 0:
        t = queue.pop()
        i = 0
        while i < z:
            aux = (val[i] + t)%10000
            if not visited[aux]:
                visited[aux] = True
                queue.appendleft(aux)
                calculado[aux] = calculado[t] + 1
            i += 1
    if(visited[y]):
        print("Case " +str(case)+ ": " +str(calculado[y]-1))
    else:
         print("Case " +str(case)+": Permanently Locked")

main()
