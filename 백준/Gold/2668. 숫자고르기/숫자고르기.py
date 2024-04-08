import sys
from itertools import combinations
input=sys.stdin.readline
ans = []
def DFS(L):
    if visit[L]==0:
        visit[L]=1
        for a in graph[L]:
            first.add(L)
            second.add(a)
            if first == second:
                ans.extend(list(second))
            DFS(a)
    visit[L]=0
n=int(input())

graph=[[] for _ in range(n+1)]
for i in range(1, n+1):
    a=int(input())
    graph[i].append(a)
    
for i in range(1, n+1):
    visit=[0]*(n+1)
    first=set()
    second=set()
    DFS(i)
ans=list(set(ans))
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
    
    
