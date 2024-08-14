from collections import deque
def solution(n,vertex):
    graph=[[]*(n+1) for i in range(n+1)]
    answer=0
    for x,y in vertex:
        graph[x].append(y)
        graph[y].append(x)
    visit=[0]*(n+1)
    distance=[int(1e9)]*(n+1)
    distance[0]=0
    def find():
        dq=deque()
        dq.append((1,0))
        distance[1]=0
        while dq:
            start, cnt=dq.popleft()
            if distance[start]<cnt:
                continue
            for next_start in graph[start]:
                if distance[next_start]>cnt+1:
                    distance[next_start]=cnt+1
                    dq.append((next_start, cnt+1))
    
    find()
    target=max(distance)
    for i in distance:
        if target==i:
            answer+=1
            
    return answer
    