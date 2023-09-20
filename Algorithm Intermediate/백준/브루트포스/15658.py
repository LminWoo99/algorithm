import sys
input=sys.stdin.readline
def DFS(L, total, plus, minus, multiply, divide):
    global maximum, minumum
    if L==n:
        maximum=max(total, maximum)
        minumum=min(total, minumum)
        return
    if plus:
        DFS(L+1, total+a[L], plus-1, minus, multiply, divide)
    if minus:
        DFS(L+1, total-a[L], plus, minus-1, multiply, divide)
    if multiply:
        DFS(L+1, total*a[L], plus, minus, multiply-1, divide)
    if divide:
        DFS(L+1, int(total/a[L]), plus, minus, multiply, divide-1)

n=int(input())
a=list(map(int, input().rstrip().split()))
op=list(map(int , input().rstrip().split()))

maximum=-1e9+1
minumum=1e9+1
DFS(1, a[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minumum)

