import sys
input=sys.stdin.readline
def Floyd():
    dist=[[INF]*(v+1) for _ in range(v+1)]
    for i in range(1, v+1):
        for dest, length in graph[i]:
            dist[i][dest]=length
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist
    
v,e=map(int, input().split())
INF=int(1e9)
graph=[[] for _ in range(v+1)] 
res=INF
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
dist=Floyd()
flag=False
for i in range(1, v+1):
    for j in range(1, v+1):
        if dist[i][j]!=INF and dist[j][i]!=INF:
            if i==j:
                res=min(res, dist[i][j])    
                flag=True
            else:
                res=min(res, dist[i][j]+dist[j][i])
                flag=True
if flag:
    print(res)
else:
    print(-1)

# import heapq as hq

# V, E = map(int, input().split())
# graph = [[] for _ in range(V+1)]
# #거리를 저장할 배열을 2차원으로
# dist = [[1e9] * (V+1) for _ in range(V+1)]

# heap = []
# for _ in range(E):
#     x, y, c = map(int, input().split())
#     graph[x].append([c, y])
#     dist[x][y] = c
#     #heap에도 비용, 출발지, 도착지 3개의 값을 넣어준다.
#     #유효한 경로 값을 다 넣어줌
#     hq.heappush(heap, [c, x, y])


# while heap:
#     #최소 비용의 경로를 먼저 뽑아주고 (d:비용, s:출발, g:도착)
#     d, s, g = hq.heappop(heap)
#     #출발지와 도착지가 같다면 사이클!
#     #heap을 이용하기 때문에 처음 나온 사이클이 가장 비용이 작은 사이클이므로 break 해버려도 됨! -> 여기서 시간이 굉장히 절약되는 듯 
#     if s == g:
#         print(d)
#         break
#     #d 값이 이미 저장된 비용보다 크다면 넘겨버림
#     if dist[s][g] < d:
#         continue
        
#     #g에서 갈 수 있는 노드들을 검사
#     for nd, ng in graph[g]:
#     	# s->g->ng로 가는 비용
#         new_d = d + nd
#         # s->g->ng로 가는게 s->ng보다 빠르다면 값 갱신해주고 heap에 넣어줌
#         if new_d < dist[s][ng]:
#             dist[s][ng] = new_d
#             hq.heappush(heap, [new_d, s, ng])
# else:
#     #heap 다 돌았는데 없다면 -1
#     print(-1)