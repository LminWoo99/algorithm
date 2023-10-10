import sys
input=sys.stdin.readline
import heapq

n=int(input())
a=[]
for i in range(n):
    x,y=map(int, input().split())
    a.append((x,y))
    
a.sort()
tmp=[]
for x in a:
    heapq.heappush(tmp, x[0])
    if len(tmp)>x[1]:
        heapq.heappop(tmp)
print(sum(tmp))