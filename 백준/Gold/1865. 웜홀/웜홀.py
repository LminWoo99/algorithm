import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
def bf(start):
    visit=[20000000]*(n+1)
    visit[start]=0
    for i in range(n):
        for cur, next, cnt in road:
            if visit[next]>visit[cur]+cnt:
                visit[next]=visit[cur]+cnt
                if i==n-1:
                    return 1  
    return 0
        
for _ in range(t):
    n,m,w=map(int, input().split())
    road=[]
    for _ in range(m):
        s,e,t=map(int, input().split())
        road.append([s,e,t])
        road.append([e,s,t])
    for _ in range(w):
        s,e,t=map(int, input().split())
        road.append([s,e,-t])
    flag=False
    if bf(1):
        flag=True
    if flag:
        print("YES")
    else:
        print("NO")