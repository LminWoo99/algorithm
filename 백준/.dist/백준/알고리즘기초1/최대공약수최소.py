import sys
a,b=map(int, sys.stdin.readline().split())
tmp=0
temp=10000
for i in range(1, min(a,b)+1):
    if a%i==0 and b%i==0:
        if tmp<i:
            tmp=i
if a%tmp==0 and b%tmp==0:
    temp=tmp*(a//tmp)*(b//tmp)
else:
    temp=a*b
print(tmp)
print(temp)
