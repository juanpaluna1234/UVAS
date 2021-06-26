"""
Ejecicio Uva 1
"""
from sys import stdin
import math

def main():
    for line in stdin:
        if line == '':
            break
        p = line.split(' ')
        binarySearch(p)
        
def binarySearch(p):
    x = .5
    ma = 1
    me = 0
    find = False
    while(find == False):
        m = operacion(x , p)
        if x == ma or x == me:
            print("No solution")
            find = True
        elif m == 0:
            print(format(round(x, 4), '.4f'))
            find = True
        elif m < 0:
            ma = x
            x = (x + me) / 2
        elif m > 0:
            me = x
            x = (x + ma) / 2
def operacion(x, aux):
    temp = int(aux[0])*math.exp(-x)+ int(aux[1])*math.sin(x) + int(aux[2])*math.cos(x) + int(aux[3])*math.tan(x) + int(aux[4])*(x**2) + int(aux[5])
    return round(temp, 5)

main()
