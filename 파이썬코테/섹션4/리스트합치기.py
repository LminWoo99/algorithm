n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
res=list(a+b)
res.sort()
print(res)
for i in range(len(res)):
    print(res[i], end=' ')