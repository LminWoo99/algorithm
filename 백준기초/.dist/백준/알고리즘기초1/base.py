import sys
a, b=map(int, sys.stdin.readline().split())
m=int(sys.stdin.readline())
res=list(map(int, sys.stdin.readline().split()))
tmp=0

for i in range(m,0 ,-1):
    result=[]
    tmp+=(a**(i-1))*res[m-i]
    temp=0
while True:
    if tmp>=b:
        temp=tmp%b
        tmp//=b
        result.append(temp)
    else:
        result.append(tmp)
        result=result[::-1]
        break
print(*result)
