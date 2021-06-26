from sys import stdin

def main():
    line = stdin.readline().strip()
    while line != "":
        line = int(line)
        periods = int(stdin.readline().strip())
        years = []
        for i in range(periods):
            year = int(stdin.readline().strip())
            years.append(year)
        popes(line, periods, years)
        line = stdin.readline()
        line = stdin.readline().strip()


def popes(rango, periods, years):
    cont = 0
    i = 0
    top = 0
    bottom = 0
    while i < periods:
        low = i
        high = periods
        b = years[i]+rango - 1
        while low < high:
            mid =  low + (int)((high - low)/2)
            if years[mid] <= b:
                low = mid+1
            else:
                high = mid
                
        cont1 = low - i
        if cont < cont1:
            top = years[low-1]
            bottom = years[i]
            cont = cont1
        i += 1
    print(cont, bottom, top)

main()
