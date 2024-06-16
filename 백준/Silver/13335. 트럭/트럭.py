import sys
input=sys.stdin.readline
from collections import deque

n,w,l=map(int, input().split())
trucks=list(map(int, input().split()))
dq=deque()
res=0
idx=0
cur_cnt=0
cur_weight=0
while True:
    res+=1
    if cur_cnt<w:
        if cur_weight+trucks[idx]<=l:
            dq.append([trucks[idx],w])
            cur_weight+=trucks[idx]
            cur_cnt+=1
            idx+=1
    if idx>=n:
        if dq:
            res+=dq[-1][1]
        print(res)
        break
    if dq:
        for truck in dq:
            truck[1]-=1
        if dq[0][1]<=0:
            cur_weight-=dq[0][0]
            dq.popleft()
            cur_cnt-=1