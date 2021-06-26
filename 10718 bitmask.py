from sys import stdin

def main():
    datos = list(map(int, stdin.readline().strip().split()))
    while datos:
        print(bitMask(datos[0],datos[1],datos[2]))
        datos = list(map(int, stdin.readline().strip().split()))

def bitMask(n,low,high):
    val = bin(n)[2::]
    if n < high:
        val1 = bin(high)[2::]
        while len(val)<len(val1):
            val = "0"+val
    i = 0
    acum = 0
    actual = len(val)-1
    num = ""
    while i < len(val):
        temp = 2**actual
        actual -= 1
        if acum+temp < low:
            num = num + "1"
            acum += temp
        elif acum+temp > high:
            num = num + "0"
        else:
            if val[i] == '0':
                num = num + "1"
                acum += temp
            elif acum < low:
                if acum + temp-1 >= low:
                    num = num + "0"
                else:
                    num = num + "1"
                    acum += temp
            else:
                num = num + "0"
        i += 1
    res = int(num,2)
    return res
main()
