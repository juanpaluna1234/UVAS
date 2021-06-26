from sys import stdin


def main():
    casos = int(stdin.readline().strip())
    while casos:
        a, b = list(map(int, stdin.readline().strip().split()))
        print(binario(adjacentMax(a,b)))
        casos -= 1

def adjacentMax(p,q):
    i = 0
    acum = ""
    while p > 1 and q > 0:
        acum = acum + "101"
        p -= 2
        q -= 1
    if q == 0 and p > 0:
        j = 0
        for j in range(p):
            acum = acum +"1"
    elif q > 0 and p == 1:
        acum = "01"+acum
    else:
        acum = "0"+acum
    return(acum)
def binario(n):
    return(int(n,2))
main()
