from collections import deque

def solution(n, computers):            
    answer = 0
    visited = [0 for i in range(len(computers))]
    def BFS(i):
        dq=deque()
        dq.append(i)
        visited[i]=1
        while dq:
            i=dq.popleft()
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    dq.append(a)
                    visited[a]=1
        
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer+=1
        
    return answer