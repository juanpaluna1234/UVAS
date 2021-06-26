"""
Ejercicio Uva 299 Train Swapping
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000000)
cont = 0
def main ():
    global cont
    cases = int(stdin.readline())
    for case in range(cases):
        tam = int(stdin.readline())
        cont = 0
        n = list(map(int, stdin.readline().strip().split()))
        mergeSort(n)
        print("Optimal train swapping takes " + str(cont) +  " swaps.")
def divideLst(n):
	res = []
	mid = int(len(n)/2)
	i = 0
	while i < mid:
		res.append(n[i])
		i += 1
	return res, n[i::]

def mergeSort(lst):
	if len(lst) == 1 or len(lst) == 0:
		return lst
	else:
		a, b = divideLst(lst)
		return concatenate( mergeSort(a), mergeSort(b))
def concatenate(a, b):
	global cont
	res = []
	i = 0
	j = 0
	while (i < len(a)) or ( j < len(b)):
		if i == len(a):
			res.append(b[j])
			j += 1
			
		elif j == len(b):
			res.append(a[i])
			i += 1
			
		else:
			if a[i] < b[j]:
				res.append(a[i])
				i += 1
				
			else:
				res.append(b[j])
				j += 1
				cont += len(a)-i
	return res

main()
