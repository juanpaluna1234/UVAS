import math
from sys import stdin
from collections import deque
adj = {}
maxDist = 0
maxNodo = 0
def main():
    global adj, maxDist, maxNodo
    line = stdin.readline().strip()
    while line != "":
        adj = {}
        maxDist = 0
        maxNodo = -1
        while line != "":
            p = line.split()
            if int(p[0]) in adj.keys(): 
                adj[int(p[0])].append([int(p[1]),int(p[2])])
            else: 
                adj[int(p[0])] = [[int(p[1]),int(p[2])]]
            if int(p[1]) in adj.keys():
                temp = adj[int(p[1])]
                adj[int(p[1])].append([int(p[0]),int(p[2])])
            else: 
                adj[int(p[1])] = [[int(p[0]),int(p[2])]]
            line = stdin.readline().strip()
        dfs(int(p[0]), -1, 0)
        dfs(maxNodo, -1, 0)
        print (maxDist)
        line = stdin.readline().strip()
        

def dfs(n, p, dist):
    global adj, maxDist, maxNodo
    for elem in adj[n]:
        if elem[0] != p:
            if elem[1] + dist > maxDist:
                maxDist = elem[1] + dist
                maxNodo = elem[0]
            dfs(elem[0], n, elem[1]+dist)

main()
    
    
    
    

