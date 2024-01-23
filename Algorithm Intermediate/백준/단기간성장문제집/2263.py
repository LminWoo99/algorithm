import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def preOrder(in_start, in_end, post_start, post_end):
    if (in_start>in_end) or (post_start>post_end):
        return
    parent=postOrder[post_end]
    print(parent, end=" ")
    
    left=position[parent]-in_start
    right=in_end-position[parent]
    
    preOrder(in_start, in_start+left-1, post_start, post_start+left-1)
    preOrder(in_end-right+1, in_end, post_end-right, post_end-1)

n=int(input())
inOrder=list(map(int, input().split()))
postOrder=list(map(int, input().split()))

position=[0]*(n+1)
for i in range(n):
    position[inOrder[i]]=i
preOrder(0, n-1, 0, n-1)