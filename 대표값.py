n=int(input())

a=list(map(int, input().split()))
x=round(sum(a)/n)
min=2147000
m=1
for idx, i in enumerate(a):
    tmp=abs(x-i)
    if tmp<min:
        min=tmp
        score=i
        res=idx+1
    elif tmp==min:
        if i>score:
            score=i
            res=idx+1
print(x, res)

        

