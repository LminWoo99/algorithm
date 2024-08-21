from collections import deque
def solution(n, computers):            
    graph=[[]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1:
                graph[i+1].append((j+1))
                graph[j+1].append((i+1))
        
    ans=0
    visit=[0]*(n+1)
    def BFS(x):
        dq=deque()
        dq.append(x)
        visit[x]=1    
        while dq:
            x=dq.popleft()
            for next_node in graph[x]:
                if not visit[next_node]:
                    visit[next_node]=1    
                    dq.append(next_node)
    for i in range(1, n+1):
        if not visit[i]:
            BFS(i)
            ans+=1
    return ans