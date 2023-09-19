import sys

input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
op=list(map(int, input().split()))

max_res = -1e9+1
min_res = 1e9+1

def DFS(depth, total, plus, minus, multiply, divide):
    global max_res, min_res
    if depth==n:
        max_res=max(max_res, total)
        min_res=min(min_res, total)
        return 
    
    if plus:
        DFS(depth+1, total+a[depth], plus-1, minus, multiply, divide)
    if minus:
        DFS(depth+1, total-a[depth], plus, minus-1, multiply, divide)
    if multiply:
        DFS(depth+1, total * a[depth], plus, minus, multiply-1, divide)
    if divide:
        DFS(depth+1, int(total/a[depth]), plus, minus, multiply, divide-1)
        
DFS(1,a[0], op[0], op[1], op[2], op[3])
print(max_res)
print(min_res)