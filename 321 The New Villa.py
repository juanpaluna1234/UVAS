from sys import stdin
from collections import deque
import copy
adj = {}
endState = ""
estados = []
def main():
    global estados, endState, adj
    line = stdin.readline().strip().split()
    r = int(line[0])
    d = int(line[1])
    s = int(line[2])
    i = 1
    while not(r == 0 and d == 0 and r == 0):
        adj = {}
        j = 1
        while j < r+1:
            adj[j] = [[],[]]
            j += 1
        j = 0
        while(j < d):
            line = stdin.readline().strip().split()
            if int(line[0]) in adj.keys():
                adj[int(line[0])][0].append(int(line[1]))
            if int(line[1]) in adj.keys():
                adj[int(line[1])][0].append(int(line[0]))
            j += 1
            
        j = 0
        while(j < s):
            line = stdin.readline().strip().split()
            if int(line[0]) in adj.keys():
                adj[int(line[0])][1].append(int(line[1]))
            j += 1
        j = 0
        
        while len(adj) > j:
            k = 0
            while(k < 2**(len(adj))):
                estados.append((binarizar(k)+str(j+1)).zfill(len(adj)+1))
                k += 1
            j += 1
        j = 0
        temp = "1".zfill(len(adj))
        temp = "1"+temp
        if(len(adj)==10):
            endState = ("1"+"0").zfill(len(adj)+1)
        else:
            endState = ("1"+str(len(adj))).zfill(len(adj)+1)
        bfs(temp,i)
        print("")
        line = stdin.readline().strip()
        line = stdin.readline().strip().split()
        r = int(line[0])
        d = int(line[1])
        s = int(line[2])
        i += 1


def bfs(inicial,w):
    global endState, adj
    queue = deque()
    queue.append([inicial,[]])
    rutas = [inicial]
    fin = False
    while(fin != True and queue):
        estado = queue.popleft()
        #print(estado)
        nodo = int(estado[0][-1])
        if(estado[0] == endState):
            fin = True
            break
        i = 0
        if nodo == 0:
            nodo = 10
        while i < len(adj[nodo][0]):
            temp = int(adj[nodo][0][i])
            if int(estado[0][temp-1]) == 1:
                aux = copy.deepcopy(estado)
                aux[0] = aux[0][:-1]
                aux[0] = aux[0] + str(temp)[-1]
                if not(aux[0] in rutas):
                    rutas.append(aux[0])
                    aux[1].append("Move to room "+ str(temp) +".")
                    queue.append(aux)
            i += 1
        i = 0
        while i < len(adj[nodo][1]):
            temp = int(adj[nodo][1][i])
            if int(estado[0][temp-1]) == 1:
                aux1 = copy.deepcopy(estado)
                aux1[0]=aux1[0][:temp-1] + '0' + aux1[0][temp:]
                if nodo != temp:
                    if not(aux1[0] in rutas):
                        rutas.append(aux1[0])
                        aux1[1].append("Switch off light in room "+ str(temp) +".")
                        queue.append(aux1)
            if int(estado[0][temp-1]) == 0:
                aux2 = copy.deepcopy(estado)
                aux2[0]=aux2[0][:temp-1] + '1' + aux2[0][temp:]
                if not(aux2[0] in rutas):
                    rutas.append(aux2[0])
                    aux2[1].append("Switch on light in room "+ str(temp) +".")
                    queue.append(aux2)
            
            i +=1
    if fin == True:
        print("Villa #"+str(w))
        print("The problem can be solved in "+str(len(estado[1]))+" steps:")
        if estado[1]: 
            for elem in estado[1]:  
                print("- "+elem)
    else:
        print("Villa #"+str(w))
        print("The problem cannot be solved.")


def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
main()

