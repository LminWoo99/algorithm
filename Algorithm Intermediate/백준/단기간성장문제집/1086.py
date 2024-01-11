import sys
input=sys.stdin.readline
from itertools import permutations
n=int(input())
a=[]
for _ in range(n):
    tmp=int(input())
    a.append(str(tmp))
k=int(input())
#분모
res=1
result=0
for i in range(n,0,-1):
    res*=i
for x in permutations(a, n):
    temp=int(''.join(x))
    if temp%k==0:
        result+=1
if result==0:
    print("0/1")
else:
    print(res)


