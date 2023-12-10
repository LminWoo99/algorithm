import sys
input=sys.stdin.readline
def soulution(n):
    n=str(n)
    tmp=int(n[1])-int(n[0])
    i=2
    temp=True
    while temp:
        if len(n)<=i:
            break
        else:
            if int(n[i])==int(n[i-1])+tmp:
                i+=1
            else:
                temp=False
    return temp
        
n=int(input())
check=[0]*(n+1)
res=99
if n<100:
    print(n)
else:
    for i in range(100, n+1):
        if soulution(i):
            res+=1
    print(res)

