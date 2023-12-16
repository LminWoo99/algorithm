import sys
input=sys.stdin.readline
from collections import deque
n, w,l=map(int, input().split())
truck=list(map(int, input().split()))
i=0
index=0
res=0
cur_weight=0
dq=deque()
dq.append(truck[0])
index+=1
time=w
while dq:
    i+=1
    time-=1
    if time==0:
        dq.popleft()
        time=w
    if len(truck)>index and sum(dq)+truck[index]<=l:
        dq.append(truck[index])
        index+=1
print(i)
# while truck:
#    if i>w:
#         res+=i
#         i=0
#         cur_weight=0
#    if len(truck)!=1 and truck[0]+cur_weight<=l:
#         x=truck.popleft()
#         cur_weight+=x
#    if len(truck)==1:
#        res+=(w+1)
#        break
#    i+=1


    
