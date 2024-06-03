import sys
input=sys.stdin.readline

def DFS(L):
    global ans
    if not visit[L]:
        visit[L]=1
        for end in graph[L]:
            first.add(L)
            second.add(end)
            if first == second:
                ans.extend(list(second))
            DFS(end)
            
n=int(input())

graph=[[] for _ in range(n+1)]
ans=[]
for i in range(n):
    graph[i+1].append(int(input()))
for i in range(1, n+1):
    first=set()
    second=set()
    visit=[0]*(n+1)
    DFS(i)
ans=list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
    print(i)