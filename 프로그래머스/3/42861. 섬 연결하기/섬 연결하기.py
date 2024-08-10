import heapq
def find(parent, x):
    if x!=parent[x]:
        parent[x]=find(parent, parent[x])
    return parent[x]
def union(parent,x,y):
    x=find(parent,x)
    y=find(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y     
def solution(n, costs):
    edges=[]
    answer = 0
    parent=[i for i in range(n)]
    for start, end, cost in costs:
        edges.append((cost, start, end))
    edges.sort()
    for edge in edges:
        if find(parent, edge[1])!=find(parent, edge[2]):
            union(parent,edge[1],edge[2])
            answer+=edge[0]
    return answer