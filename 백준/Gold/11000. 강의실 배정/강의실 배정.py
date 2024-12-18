import sys,heapq
input=sys.stdin.readline

n=int(input())
lessons=[]
for _ in range(n):
    s,t=map(int, input().split())
    lessons.append([s,t])
lessons.sort(key=lambda x:(x[0], x[1]))
hq=[lessons[0][1]]
for i in range(1, n):
    if hq[0] <= lessons[i][0]:
        heapq.heappop(hq)
    heapq.heappush(hq, lessons[i][1])
print(len(hq)) 
