n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=[[0]*(n+2) for _ in range(n+2)]
# [0] 값을 가장자리에 모두 둘렀음
for x in range(n):
    for y in range(n):
        if x<n+2 and y<n+2:
            m[x+1][y+1]=a[x][y]
res=0
for i in range(1, n):
    for j in range(n):
        if m[i][j-1]<m[i][j] and m[i-1][j]<m[i][j] and m[i][j+1]<m[i][j] and m[i+1][j]<m[i][j]:
            res +=1
print(res)       
