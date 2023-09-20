from collections import deque
def bfs(x):
    dq=deque()
    dq.append(x)
    while dq:
        x=dq.popleft()
        if x==m:
            return a[m]
        for xx in (x-1, x+1, x*2):
            if 0<=xx<=100000 and not a[xx]:
                a[xx]=a[x]+1
                dq.append(xx)
                
n, m=map(int, input().split())
a=[0]*100001
print(bfs(n))