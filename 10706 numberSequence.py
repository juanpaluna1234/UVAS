from sys import stdin

num1 = []
k = 1
def main():
    cases = int(stdin.readline().strip())
    case = 0
    aux = []
    cont = 0
    while case < cases:
        line = int(stdin.readline().strip())
        if cont < line:
            cont = line
            num = sec(line, aux)
        sequence(line, cont, num)
        case += 1
        
def sec(n, temp):
    if not temp:
        temp = [1,3]
        i = 3
        j = 1
    else:
        i = temp[len(temp)-1]
        j = len(temp)-1
    while temp[len(temp)-1] < n:
        #digit = 0
        temp1 = i
        digit = len(str(i))
        #while temp1 > 0:
         #   temp1 = temp1//10
          #  digit += 1
        temp.append(temp[j]-temp[j-1]+digit+temp[j])
        i += 1
        j += 1
    return temp
def sequence(aux, n, num):
    low = 0
    high = len(num)
    b = aux
    while low < high:
        mid =  low + ((high - low)>>1)
        if num[mid] == b:
            low = mid
            break
        if num[mid] <= b:
            low = mid+1
        else:
            high = mid
    if num[low] != 1:
        generar(low, b-num[low-1])
    else:
        print(1)
        
def generar(n, m):
    global num1, k
    while len(num1) <= m-1:
        temp = str(k)
        j = 0
        while j < len(temp):
            num1.append(int(temp[j]))
            j += 1
        k += 1
    print(num1[m-1])
main()
