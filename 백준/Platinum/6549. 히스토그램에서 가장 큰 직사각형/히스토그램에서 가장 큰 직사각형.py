import sys
input = sys.stdin.readline
while True:
    n, *a = map(int, input().split())
    if n == 0:
        break
    a.append(0)
    stack=[-1]
    res=0
    for i in range(n+1):
        while stack and a[stack[-1]]>a[i]:
            height=a[stack.pop()]
            width=i-stack[-1]-1
            res=max(res, height*width)
        stack.append(i)
    print(res)