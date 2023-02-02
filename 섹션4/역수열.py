n=int(input())
a=list(map(int, input().split()))
tmp=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and tmp[j]==0:
            tmp[j]=i+1
            break
        elif tmp[j]==0:
            a[i]-=1

for x in tmp:
    print(x, end=' ')