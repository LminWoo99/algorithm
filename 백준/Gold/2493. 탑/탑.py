import sys
input=sys.stdin.readline

n=int(input())
top=list(map(int, input().split()))
stack=[]
stack.append((0,0))
res=[0]*n
for i in range(n):
    cur=top[i]
    while stack:
        if stack[-1][1]<i and stack[-1][0]>cur:
            res[i]=stack[-1][1]+1
            break
        else:
            if not stack:
                res[i]=0
                break
            stack.pop()
    stack.append((top[i],i))
print(*res)
