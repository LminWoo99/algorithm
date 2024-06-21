import sys
input=sys.stdin.readline
from itertools import combinations
def solution(tmp_list):
    tmp=0
    for home in home_list:
        cur=int(1e9)
        for chicken in tmp_list:
            cur=min(abs(home[0]-chicken[0])+abs(home[1]-chicken[1]),cur)
        tmp+=cur
        if tmp>res:
            break
    return tmp
n,m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
## 치킨집을 고르고 bfs()?
home_list=[]
chicken_list=[]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            home_list.append((i,j))
        elif board[i][j]==2:
            chicken_list.append((i,j))
res=int(1e9)
for i in combinations(chicken_list, m):
    res=min(solution(i),res)
print(res)