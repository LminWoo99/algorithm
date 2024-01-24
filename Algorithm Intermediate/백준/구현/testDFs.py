import sys,heapq
n,m = map(int, sys.stdin.readline().rstrip().split())

res = []
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n+1)]
hq = []
for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    degree[y] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(hq, i)

while hq:
    tmp = heapq.heappop(hq)
    res.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(hq, i)

print(" ".join(map(str, res)))