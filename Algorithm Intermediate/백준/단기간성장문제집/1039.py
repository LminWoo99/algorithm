import sys
input=sys.stdin.readline
from collections import deque
def BFS(n,k):
    visit=set()
    visit.add((n,0))
    dq=deque()
    dq.append((n,0))
    ans=0
    while dq:
        n,cnt =dq.popleft()
        if cnt==k:
            ans=max(ans, n)
            continue
        n=list(str(n))
        for i in range(m-1):
            for j in range(i+1, m):
                if i==0 and n[j]=='0':
                    continue
                n[i], n[j]=n[j],n[i]
                new=int(''.join(n))
                if (new, cnt+1) not in visit:
                    dq.append((new, cnt+1))
                    visit.add((new, cnt+1))
                n[i], n[j]=n[j],n[i]
    if ans:
        return ans
    else:
        return -1

n,k=map(int, input().split())
m=len(str(n))
print(BFS(n,k))