import sys
input=sys.stdin.readline
from collections import deque
def BFS(s, cnt):
    dq=deque()
    dq.append((s,cnt))
    global boolean
    while dq:
        s,cnt=dq.popleft()
        if s==G:
           return cnt
        else:
            if s+U<=F and U!=0 and visit[s+U]==0:
                visit[s+U]=1
                dq.append((s+U,cnt+1))
            if s-D>=1 and D!=0 and visit[s-D]==0:
                visit[s-D]=1
                dq.append((s-D, cnt+1))    
F, S, G, U, D=map(int, input().split())
tmp=0
cnt=0
visit=[0]*(1000001)
if S == G:
	print(0)
else:
    res=BFS(S, cnt)
    if res:
        print(res)
    else:
        print("use the stairs")
