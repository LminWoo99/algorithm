import sys , heapq
input=sys.stdin.readline
hq=[]
for _ in range(int(input())):
    tmp=int(input())
    if tmp:
        heapq.heappush(hq, -tmp)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)