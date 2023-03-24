from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split()))for _ in range(n)]
dq=deque()
ch=[[0]*n for _ in range(n)]
sum=0
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
dq.append((n//2, n//2))
print(dq[0])
L=0
while True:
    if L==n//2:
        break
    size=len(dq)
    for i in range(size):
        tmp=dq.popleft()
        print(tmp[0], tmp[1])
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                dq.append((x,y))
    L+=1
print(sum)

    
# 10 13 10 12 15 
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
