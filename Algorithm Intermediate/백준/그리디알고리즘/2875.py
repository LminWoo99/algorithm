import sys
input=sys.stdin.readline
team=0
n,m,k=map(int, input().split())
while True:
    n-=2
    m-=1
    if n<0 or m<0 or (n+m)<k:
        break
    team+=1
print(team)