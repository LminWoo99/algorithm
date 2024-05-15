import sys
input=sys.stdin.readline
from collections import deque
n,k=map(int, input().split())

m=len(str(n))
def BFS(n,k):
    visit=set()
    visit.add((n,0))
    dq=deque()
    dq.append((n,0))
    ans=0
    while dq:
        n, cnt=dq.popleft()
        if cnt==k:
            ans=max(ans, n)
            continue
        n=list(str(n))
        for i in range(m-1):
            for j in range(i+1, m):
                if i==0 and n[j]=='0':
                    continue
                n[i], n[j]=n[j], n[i]
                nn=int(''.join(n))
                if (nn,cnt+1) not in visit:
                    visit.add((nn, cnt+1))
                    dq.append((nn,cnt+1))
                n[i], n[j]=n[j], n[i]
    return ans if ans else -1;
res=BFS(n,k)
print(res)

