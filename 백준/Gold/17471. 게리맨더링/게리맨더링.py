import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

def BFS(list):
    dq=deque()
    dq.append(list[0])
    visit=set()
    visit.add(list[0])
    total_population=0
    while dq:
        i=dq.popleft()
        total_population+=population[i]
        for next_i in graph[i]:
            if next_i not in visit and next_i in list:
                visit.add(next_i)
                dq.append(next_i)
    return total_population, len(visit)
        
    
n=int(input())
population=[0]+list(map(int, input().split())) # 구역 인구
graph=[[]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    adjoin_list=list(map(int, input().split()))
    if len(adjoin_list)!=1:
        cnt=adjoin_list.pop(0)
        for x in adjoin_list:
            graph[i].append(x)
comb_list=[i for i in range(1,n+1)]
res=int(1e9)
for i in range(1, n//2+1):
    for tmp_list in combinations(comb_list, i):
        cnt1, sum1=BFS(tmp_list)
        spare_list=[i for i in range(1, n+1) if i not in tmp_list]
        cnt2, sum2=BFS(spare_list)
        if sum1+sum2==n:
            res=min(res, abs(cnt1-cnt2)) 
if res==int(1e9):
    res=-1
print(res)