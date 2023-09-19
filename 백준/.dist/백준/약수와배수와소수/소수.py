n=int(input())
m=int(input())
a=[]
for i in range(n,m+1):
    res=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                res+=1
        if res==0:
            a.append(i)
if len(a)!=0:
    print(sum(a))
    print(min(a))
else:
    print(-1)

    
        