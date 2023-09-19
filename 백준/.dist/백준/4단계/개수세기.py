n=int(input())
a=list(map(int, input().split()))
v=int(input())
res=0
for i in a:
    if i==v:
        res+=1
print(res)