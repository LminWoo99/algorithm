n, k=map(int, input().split())
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=1
    if s==k:
        print(i)
        break
else:
    print(-1)