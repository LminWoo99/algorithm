import sys
input=sys.stdin.readline
import heapq

## 짝수면 중간에 있는 두수중 작은수 왼쪽
n=int(input())
a=[]
left=[]
# 작은거 리스트에서 가장 큰 값 보다 크면 right, 작으면 left
right=[]
for _ in range(n):
    x=int(input())
    a.append(x)
    if len(left)==len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    if right and right[0]<-left[0]:
        left_val=heapq.heappop(left)
        right_val=heapq.heappop(right)

        heapq.heappush(left, -right_val)
        heapq.heappush(right,- left_val)
    print(-left[0])