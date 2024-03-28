import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        graph[y]=x
    else:
        graph[x]=y
n=int(input())
m=int(input())

graph=[i for i in range(n+1)]
for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j]==1:
           union(i+1, j+1)
           

# 여행 계획

plan=list(map(int, input().split()))
answer=[]
for i in range(len(plan)):
    answer.append(graph[plan[i]])
answer=list(set(answer))
if len(answer)==1:
    print("YES")
else:
    print("NO")
