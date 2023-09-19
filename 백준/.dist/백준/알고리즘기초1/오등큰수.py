import sys
from collections import Counter
n=int(input())
a=list(map(int, sys.stdin.readline().split()))
answer=[-1]*n
counter=Counter(a)
stack=[]
stack.append(0)
for i in range(1, n):
    while stack and counter[a[stack[-1]]]<counter[a[i]]:
        answer[stack.pop()]=a[i]
    stack.append(i)
print(*answer)
