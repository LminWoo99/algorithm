import sys
input=sys.stdin.readline
import heapq

n=int(input())
left=[]
right=[]
for i in range(n):
    num=int(input())
    if len(left)==len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    if right and right[0]<-left[0]:
        leftRes=heapq.heappop(left)
        rightRes=heapq.heappop(right)
        
        heapq.heappush(left, -rightRes)
        heapq.heappush(right, -leftRes)
    print(-left[0])
