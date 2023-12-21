import sys
input=sys.stdin.readline

def check():
    global cnt
    for i in range(n):
        now = i
        for j in range(h):
            if line[j][now]:
                now+=1
            elif now>0 and line[j][now-1]:
                now -=1
        if now != i:
            return False
    return True
def DFS(cnt , x ,y):
    global ans
    if check():
        ans=min(ans, cnt)
        return
    elif cnt==3 or ans<=cnt:
        return
    for i in range(x, h):
        if i==x:
            now = y
        else:
            now=0
        for j in range(now, n-1):
            if not line[i][j] and not line[i][j+1]:
                if j>0 and line[i][j-1]:
                    continue
                line[i][j]=True
                DFS(cnt+1, i, j+2)
                line[i][j]=False
    
                
n,m,h =map(int, input().split())
ans=4
if m==0:
    print(0)
else:
    cnt=0
    line=[[False]*n for _ in range(h)]
    for i in range(m):
        a,b=map(int, input().split())
        line[a-1][b-1]=True
    DFS(0,0,0)
    print(ans if ans < 4 else -1)