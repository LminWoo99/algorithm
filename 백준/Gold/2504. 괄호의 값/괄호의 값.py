import sys
input=sys.stdin.readline

a=input().rstrip()
stack=[]
res=0
tmp=1
for x in range(len(a)):
    if a[x]=='(':
        stack.append(a[x])
        tmp*=2
    elif a[x]=='[':
        stack.append(a[x])
        tmp*=3
    elif a[x]==')':
        if not stack or stack[-1]=='[':
            res=0
            break
        if a[x-1]=='(':
            res+=tmp
        stack.pop()
        tmp//=2
    else:
        if not stack or stack[-1]=='(':
            res=0
            break
        if a[x-1]=='[':
            res+=tmp
        stack.pop()
        tmp//=3
if stack:
    print(0)
else:
    print(res)
            
            
        
    