import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

res=[]
tmp=set(a)&set(b)
while tmp:
    max_val=max(tmp)
    res.append(max_val)   
    
    a1=a.index(max_val)
    b1=b.index(max_val)
    
    a=a[a1+1:]
    b=b[b1+1:]
    
    tmp=set(a)&set(b)
    
print(len(res))
print(*res)