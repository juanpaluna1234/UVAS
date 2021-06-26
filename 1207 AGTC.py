from sys import stdin

#referencia: https://www.youtube.com/watch?v=We3YDTzNXEk&ab_channel=TusharRoy-CodingMadeSimple

def main():
    str1 = stdin.readline().strip().split()
    while (str1):
        str1[0] = int(str1[0])
        str2 = stdin.readline().strip().split()
        str2[0] = int(str2[0])
        agtc(str1, str2)
        str1 = stdin.readline().strip().split()
    
def agtc(str1,str2):
    dif = str1[0] - str2[0]
    while dif < 0:
        str1[1] = str1[1] + " "
        dif += 1
    while dif > 0:
        str2[1] = str2[1] + " "
        dif -= 1
    tabla = [[0]]
    i = 1
    while i <= str1[0]:
        tabla[0].append(i)
        i += 1
    i = 1
    while i <= str2[0]:
        tabla.append([i])
        i += 1
    i = 1
    while i <= str1[0]:
        j = 1
        while j <= str2[0]:
            if(str1[1][i-1] == str2[1][j-1]):
                tabla[j].append(tabla[j-1][i-1])
            else:
                aux = min(tabla[j-1][i-1], min(tabla[j][i-1], tabla[j-1][i]))+1
                tabla[j].append(aux)
            j += 1
        i+= 1
    print(tabla[str2[0]][str1[0]])

main()
