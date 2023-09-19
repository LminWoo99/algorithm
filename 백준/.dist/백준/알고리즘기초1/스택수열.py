n=int(input())
res=[]
stack=[]
cur=1
flag=0
for i in range(n):
    a=int(input())
    while cur<=a:
        stack.append(cur)
        res.append('+')
        cur+=1
    if stack[-1]==a:
        stack.pop()
        res.append('-')
    else:
        print("NO")
        flag=1
        break
if flag==0:
    for i in res:
        print(i)
