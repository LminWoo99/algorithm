import sys
input=sys.stdin.readline

n, m=map(int, input().split())
a=[list(map(int, input().rstrip())) for _ in range(n)]
b=[list(map(int, input().rstrip())) for _ in range(n)]
cnt=0
if a==b:
    print(0)
else:        
    if n<3 or m<3:
        print(-1)    
    else:
        while True:
            for i in range(n-2):
                for j in range(m-2):
                    if a[i][j]!=b[i][j]:
                        for x in range(i, i+3):
                            for y in range(j, j+3):
                                if a[x][y]==1:
                                    a[x][y]=0
                                else:
                                    a[x][y]=1
                                    
                        cnt+=1
                    else:
                        continue
                    
            if a != b:
                print(-1)
                break
            else:
                print(cnt)
                break
        