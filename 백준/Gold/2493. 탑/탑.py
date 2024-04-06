import sys
input=sys.stdin.readline

n=int(input())
top=list(map(int, input().split()))
stack=[]
res=[0]*(len(top))
for i in range(n):
    while stack:
        if stack[-1][1]>top[i]:
            res[i]=stack[-1][0]+1
            break
        else:
            stack.pop()

    stack.append((i, top[i]))
        
print(*res)