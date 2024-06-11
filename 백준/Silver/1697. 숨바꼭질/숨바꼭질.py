import sys
input=sys.stdin.readline
from collections import deque
visit=[0]*100001
def BFS(L):
    dq=deque()   
    dq.append((L,0))
    visit[L]=1
    while dq:
        L,cnt=dq.popleft()
        if L==k:
            return cnt
        for i in (L-1, L+1, L*2):
            if 0<=i<=100000 and not visit[i]:
                visit[i]=1
                dq.append((i,cnt+1))
n,k=map(int, input().split())
res=BFS(n)
print(res)