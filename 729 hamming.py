from sys import stdin
import math
def main():
    global cosa
    casos = int(stdin.readline().strip())
    stdin.readline()
    while casos:
        n, h = list(map(int, stdin.readline().strip().split()))
        hamming2("",n,h)
        if casos > 1:
            print("")
        stdin.readline()
        casos -= 1
    
def hamming(n, h):
    existencias = []
    p = math.factorial(n)/(math.factorial(n-h)*math.factorial(h))
    a = 0
    while len(existencias) < p:
        x = bin(a)[2::]
        if x.count('1') == h:
            i = 0
            while len(x) < n:
                x = '0'+x
            print(x)
        a += 1

def hamming2(x,n,h):
    if h == 0:
        while n:
            x = x+'0'
            n -= 1
        print(x)
        return 0
    elif h > 0 and n > 0 and n >= h:
        hamming2(x+'0',n-1,h)
        hamming2(x+'1',n-1,h-1)
        return 0
    else:
        return 0
main()

