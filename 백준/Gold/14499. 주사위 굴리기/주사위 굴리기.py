import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def roll(dice, order):
    a,b,c,d,e,f=dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if order==1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=c,b,f,a,e,d
    elif order==2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=d,b,a,f,e,c
    elif order==3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=b,f,c,d,a,e
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=e,a,c,d,f,b
        
    
n,m,x,y,k=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
orders=list(map(int, input().rstrip().split()))
# index 0: 지도랑 닿으면, 1: 남쪽, 2: 동쪽, 북쪽 :4, 서쪽 3
dice=[0]*6
for order in orders:
    xx,yy=x+dx[order-1],y+dy[order-1]
    if 0<=xx<n and 0<=yy<m:
        roll(dice,order)
        if maps[xx][yy]:
            dice[0]=maps[xx][yy]
            maps[xx][yy]=0
        else:
            maps[xx][yy]=dice[0]
        
        print(dice[5])
        x,y=xx,yy