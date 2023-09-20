n, m=map(int, input().split())
score=[]
dy=[0]*(m+1)
ch=[0]*n
for i in range(n):
    a,b=map(int, input().split())
    for j in range(m, b-1, -1):
        dy[j]=max(dy[j-b]+a, dy[j])
print(dy[m])

    