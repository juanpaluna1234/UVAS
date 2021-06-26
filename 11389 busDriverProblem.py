from sys import stdin

def main():
    n,d,r = list(map(int, stdin.readline().strip().split()))
    while n != 0 and d != 0 and r != 0:
        dia = list(map(int, stdin.readline().strip().split()))
        noche = list(map(int, stdin.readline().strip().split()))
        print(busDriver(dia,noche,n,r,d))
        n,d,r = list(map(int, stdin.readline().strip().split()))
def busDriver(dia,noche,n,r,d):
    dia.sort()
    noche.sort()
    i = 0
    acum = 0
    while i < n:
        acum = acum + max(dia[i]+noche[len(noche)-1-i]-d,0)
        i += 1
    acum = acum*r
    return(acum)
main()
