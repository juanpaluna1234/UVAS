import math
from sys import stdin
from collections import deque
postFinal = ""
def main ():
    global postFinal
    empezo = False
    cases = int(stdin.readline().strip())

    for case in range(cases):
        a, b, c = list(map(str, stdin.readline().strip().split()))
        postFinal = ""
        preInPost(b, c)
        print (postFinal)
def preInPost(preorder, inorder):
    global postFinal
    if(len(inorder) == 1):
        postFinal = postFinal + inorder
    elif (len(inorder) > 0):
        if preorder[0] in inorder: 
            root = inorder.index(preorder[0])
        left_in = inorder[:root]
        right_in = inorder[root+1:]
        left_pre = preorder[1:len(left_in)]
        right_pre = preorder[len(left_in)+1:]
        if(len(left_in) == 1):
            postFinal = postFinal + left_in
        elif (left_in != ""):
            preInPost(left_pre, left_in)
        if(len(right_in) == 1):
            postFinal = postFinal + right_in
        elif (right_in != ""):
            preInPost(right_pre, right_in)
        postFinal = postFinal + preorder[0]

main()
