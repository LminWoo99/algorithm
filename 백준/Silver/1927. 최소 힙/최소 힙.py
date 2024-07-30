import heapq, sys
input=sys.stdin.readline

hq=[]
for _ in range(int(input())):
    tmp=int(input())
    if not tmp:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
        continue
    heapq.heappush(hq, tmp)