import sys
import heapq
input=sys.stdin.readline
def solution(n,k):
    
    heapq.heappush(hq, (0, n))
    distance[n]=0
    while hq:
        dist, start=heapq.heappop(hq)
        if distance[start]<dist:
            continue
        for x in (start-1, start+1, start*2):
            if 0<=x<100001:
                if start*2==x and distance[x]>dist:
                    distance[x]=dist
                    heapq.heappush(hq, (dist, x))
                elif start*2!=x:
                    if distance[x]>dist+1:
                        distance[x]=dist+1
                        heapq.heappush(hq, (dist+1, x))
                    
n, k =map(int, input().split())
distance=[int(1e9)]*100001
hq=[]
solution(n,k)
print(distance[k])