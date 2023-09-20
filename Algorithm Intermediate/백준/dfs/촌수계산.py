import sys
input=sys.stdin.readline
def dfs(cnt, depth):
    visit[cnt]=1
    depth+=1
    if cnt==b:
        result.append(depth)
    for i in graph[cnt]:
        if visit[i]==0:
            dfs(i, depth)
n=int(input())
a,b=map(int, input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)
result=[]
for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a,0)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)