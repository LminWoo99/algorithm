import sys
from collections import deque
input=sys.stdin.readline

def BFS():
    visit=set()
    visit.add((n, 0))
    dq=deque()
    dq.append((n,0))
    ans=-1
    while dq:
        val, idx=dq.popleft()
        if idx==k:
            ans=max(val, ans)
            continue
        val=list(str(val))
        for i in range(m-1):
            for j in range(i+1, m):
                if i==0 and val[j]=='0':
                    continue
                val[i], val[j]= val[j], val[i]
                new_val=int(''.join(val))
                if (new_val, idx+1) not in visit:
                    visit.add((new_val, idx+1))
                    dq.append((new_val, idx+1))
                val[i], val[j]= val[j], val[i]
    return ans
n,k = map(int, input().split())
m=len(str(n))

print(BFS())