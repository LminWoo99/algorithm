import sys
from itertools import combinations
input=sys.stdin.readline
def solve(x):
    res=0
    for i in range(len(x)):
        for j in range(i, len(x)):
            res+=score[x[j]-1][x[i]-1]
            res+=score[x[i]-1][x[j]-1]
    return res

n=int(input())
score=[list(map(int, input().split())) for _ in range(n)] 
team=[]
result=10000
for i in range(1, n+1):
    team.append(i)
for i in combinations(team, n//2):
    res=solve(i)
    team_b=[]
    for j in team:
        if j not in i:
            team_b.append(j)
    res_2=solve(team_b)
    result=min(result, abs(res-res_2))
print(result)

    
