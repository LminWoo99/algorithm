n=int(input())
a=[[0]*100 for _ in range(100)]
res=0
for _ in range(n):
    y,x=map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            a[i][j]=1
for k in range(100):
    res+=a[k].count(1)
print(res)
        
    