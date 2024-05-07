import sys
import heapq
input=sys.stdin.readline

n=int(input())
cards=[]
hq=[]
res=0
for _ in range(n):
    cards.append(int(input()))


for card in cards:
    heapq.heappush(hq, card)
while len(hq)>1:
    x=heapq.heappop(hq)
    y=heapq.heappop(hq)
    res+=(x+y)
    heapq.heappush(hq, (x+y))
print(res)