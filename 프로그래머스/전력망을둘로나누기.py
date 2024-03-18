from collections import deque    
def solution(n, wires):
    answer = -1
    graph=[[] for _ in range(n+1)]

    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    def bfs(start):
        dq=deque()
        visit=[0]*(n+1)
        dq.append(start)
        cnt=1
        visit[start]=1
        while dq:
            x=dq.popleft()
            for i in graph[x]:
                if not visit[i]:
                    dq.append(i)
                    visit[i]=1
                    cnt+=1
        return cnt
    answer=n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer=min(answer, abs(bfs(a)-bfs(b)))
        graph[a].append(b)
        graph[b].append(a)


    
    return answer