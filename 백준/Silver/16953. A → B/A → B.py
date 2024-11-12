import sys
from collections import deque
input=sys.stdin.readline

a,b=map(int, input().split())
dq=deque()
dq.append((a,1))
ans=-1
while dq:
    cur_val, cnt= dq.popleft()
    if cur_val==b:
        ans=cnt
        break
    elif cur_val>b:
        continue
    dq.append((cur_val*2, cnt+1))
    dq.append((int(str(cur_val)+'1'), cnt+1))
print(ans)