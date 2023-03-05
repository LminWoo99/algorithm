n=int(input())
res=list()
'''
for i in range(n):
        temp=list(map(int, input().split()))
        tp=set(temp)
        if len(tp)==1:
            tp=list(tp)
            res.append(10000+tp[0]*1000)
        elif len(tp)==2:
            tp=list(tp)
            for x in tp:
                if x not in temp:
                    res.append(1000+tp[0]*100)
        else:
            res.append(max(temp)*100)
print(res, end=' ')
print(max(res))   
'''
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split() 
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)


