n, m=map(int, input().split())
a=[]
dy=[0]*(m+1)
for i in range(n):
    x,y=map(int,input().split())
    for j in range(x, m+1):
        dy[j]=max(dy[j], dy[j-x]+y)
        
print(dy[m])

