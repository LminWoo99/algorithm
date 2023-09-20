import sys
input=sys.stdin.readline
def back(L):
    global w, maximum
    if len(w)==2:
        maximum=max(L, maximum)
    for i in range(1,len(w)-1):
        tmp=w[i]
        left=w[i-1]
        right=w[i+1]
        w.pop(i)
        back(L+left*right)
        w.insert(i, tmp)
n=int(input())
w=list(map(int, input().split()))

maximum=0
back(0)
print(maximum)
