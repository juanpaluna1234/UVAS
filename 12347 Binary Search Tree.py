from sys import stdin
import math

def main():
    p = []
    for line in stdin:
        if line == "\n":
            break
        line.strip()
        p.append(int(line))
    i = 0
    while(p[0] >= p[i]):
        i = i + 1
    first_half = p[1:i]
    second_half = p[i:]
    binaryTreeSearch(p[0],first_half,second_half)

def binaryTreeSearch(root, left, right):
    if(len(left) == 1):
        print(left[0])
    elif (left != []):
        i = 0
        while(i < len(left) and left[0] >= left[i]):
            i = i + 1
        first_left = left[1:i]
        second_left = left[i:]
        binaryTreeSearch(left[0],first_left,second_left)
    if(len(right) == 1):
        print(right[0])
    elif (right != []):
        i = 0
        while( i < len(right) and right[0] >= right[i]):
            i = i + 1
        first_right = right[1:i]
        second_right = right[i:]
        binaryTreeSearch(right[0],first_right,second_right)
    print (root)
    
main()
