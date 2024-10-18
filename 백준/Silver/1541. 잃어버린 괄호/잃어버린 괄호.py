import sys
input=sys.stdin.readline
a=input().rstrip()
a=a.split('-')

num=[]
for i in a:
    x=0
    tmp=i.split('+')
    for j in tmp:
        x+=int(j)
    num.append(x)
ans=num[0]
for i in range(1, len(num)):
    ans-=num[i]
print(ans)