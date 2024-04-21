import sys
input=sys.stdin.readline
from collections import deque
dx=[-1, -1, 0, 1, 1,1,0,-1]
dy=[0,1, 1, 1, 0, -1, -1, -1]

n,m,k=map(int, input().split())
board=[[[] for _ in range(n)] for _ in range(n)]
fireballs = []
for _ in range(m):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r-1, c-1, m, s, d]) # 행, 열 , 질량, 속도, 방향


for _ in range(k):
    while fireballs:
        r,c,m,s,d=fireballs.pop(0)
        rr=(r+s*dx[d])%n
        cc=(c+s*dy[d])%n
        board[rr][cc].append([m,s,d])
    for i in range(n):
        for j in range(n):
            if len(board[i][j])>=2:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[i][j])
                while board[i][j]:
                    _m, _s, _d=board[i][j].pop(0)
                    sum_m+=_m
                    sum_s+=_s
                    if _d%2==0:
                        cnt_odd+=1
                    else:
                        cnt_even+=1
                if cnt_odd==cnt or cnt_even==cnt:
                    nd=[0,2,4,6]
                else:
                    nd=[1,3,5,7]
                if sum_m//5:
                    for d in nd:
                        fireballs.append([i,j,sum_m//5, sum_s//cnt, d])
            if len(board[i][j])==1:
                fireballs.append([i,j]+board[i][j].pop())
print(sum([fireball[2] for fireball in fireballs]))
