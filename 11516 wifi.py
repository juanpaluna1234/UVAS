from sys import stdin
n = 0
m = 0
router = []
def main():
    global n,m,router
    cases = int(stdin.readline().strip())
    while cases:
        n, m = list(map(int, stdin.readline().strip().split()))
        if n >= m:
            print("0.0")
            while m:
                m -= 1
                caso = int(stdin.readline().strip())
        else:
            i = 0
            router = []
            while i < m:
                caso = int(stdin.readline().strip())
                router.append(caso)
                i += 1
            router.sort()
            
            print("{:.1f}".format(search(0,router[len(router)-1])/2))
        cases -= 1
def search(low,high):
    global n,m,router
    mid = 0
    while high - low > 1:
        mid = int((low + high)/2)
        if (wifi(mid)):
            high = mid
        else:
            low = mid
    return high
def wifi(val):
    global m,n,router
    aux = 1
    rango = router[0]+val
    i = 1
    while i < len(router):
        if router[i] > rango:
            aux += 1
            rango = router[i]+val
        i += 1
    return aux <= n

main()
