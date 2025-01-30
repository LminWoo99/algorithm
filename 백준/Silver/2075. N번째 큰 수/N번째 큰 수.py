import sys , heapq
input=sys.stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
hq=[]

for i in range(n):
    for j in range(n):
        if len(hq) < n:
            heapq.heappush(hq, a[i][j])
        else:
            if hq[0] < a[i][j]:
                heapq.heappop(hq)
                heapq.heappush(hq, a[i][j])
print(hq[0])