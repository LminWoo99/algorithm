import sys
input=sys.stdin.readline
a=[]
for i in range(9):
    tmp=int(input())
    a.append(tmp)
a.sort()
temp=sum(a)
x=0
y=0
for k in range(9):
    for j in range(k+1, 9):
        if (temp-a[k]-a[j])==100:
            x=a[k]
            y=a[j]
a.remove(x)            
a.remove(y)
for i in a:
    print(i)