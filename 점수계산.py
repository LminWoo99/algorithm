n=int(input())
a=list(map(int, input().split()))
p=1
res=0
for i in range(len(a)):
    if a[i]==1:
        res +=p
        p+=1
    else:
        res +=0
        p=1
print(res)