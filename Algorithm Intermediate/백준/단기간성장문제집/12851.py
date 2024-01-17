import sys
input=sys.stdin.readline
from collections import deque
def BFS(n):
    dq=deque()
    dq.append(n)
    while dq:
       x=dq.popleft()
       if x==k:
           return visit[k]
       for xx in (x-1, x+1, x*2):
           if 0<=xx<=100000 and not visit[xx]:
               visit[xx]=visit[x]+1
               path[xx]=x
               dq.append(xx)
    
n,k=map(int, input().split())
visit=[0]*100001
path=[0]*100001
res=BFS(n)
print(res)
result=[]
result.append(k)
for i in range(res):
    result.append(path[result[-1]])
result=result[::-1]
print(*result)

