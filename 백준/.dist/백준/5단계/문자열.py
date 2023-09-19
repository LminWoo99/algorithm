n=int(input())
res=[]
for i in range(n):
    a=input()
    res.append(a[0]+a[-1])
for i in range(len(res)):
    print(res[i])