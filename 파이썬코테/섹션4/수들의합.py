n, m=map(int, input().split())
a=list(map(int, input().split()))
res=0
j=0
for i in range(len(a)):
    temp=0
    temp+=a[i]
    for j in range(i+1,len(a)):
        temp+=a[j]
        if temp == m or a[j]==m:
            res+=1
            break
print(res)