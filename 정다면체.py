n,m=map(int, input().split())
a=[]
b=list(0 for i in range(0, n*m+1))
result=0
for i in range(1,n+1):
    for j in range(1,m+1):
        a.append(i+j)
for k in range(2,len(a)):
    b[k]=a.count(k)
result=max(b)   
for m in range(len(b)):
    if b[m]==result:
        print(m, end=' ')   
    
