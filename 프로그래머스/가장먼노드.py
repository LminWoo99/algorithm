from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    distance=[0]*(n+1)
    dq=deque()
    dq.append((1, 0))
    while dq:
        x,cnt=dq.popleft()
        for i in graph[x]:
            if distance[i]==0 and i!=1:
                distance[i]=cnt+1
                dq.append((i, cnt+1))
    tmp=max(distance)
    for i in range(len(distance)):
        if distance[i]==tmp:
            answer+=1
    return answer