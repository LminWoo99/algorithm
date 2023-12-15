import sys
input=sys.stdin.readline
from itertools import combinations

    
    
n,m =map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]

chicken=[]
home=[]

result=99999
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            chicken.append((i,j))
        elif board[i][j]==1:
            home.append((i,j))

for chick in combinations(chicken, m):
    temp=0
    for h in home:
        chick_len=999
        for j in range(m):
            chick_len=min(chick_len, abs(h[0]-chick[j][0])+abs(h[1]- chick[j][1]))
        temp+=chick_len
    result=min(temp, result)

print(result)