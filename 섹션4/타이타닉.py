n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
res=0
while a:
    if len(a)==1:
        res+=1
        break
    if a[0]+a[-1]>m:
        a.pop()
        res+=1
    else:
        a.pop(0)
        a.pop()
        res+=1
print(res)
    
         