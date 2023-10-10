import sys
import heapq
input=sys.stdin.readline
n,k = map(int,input().split())
gem = [[*map(int,input().split())] for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort();bag.sort()
result = 0;tmp = [] 
 
for bag in bag:
    while gem and gem[0][0] <= bag:
        heapq.heappush(tmp, -gem[0][1])
        heapq.heappop(gem)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
