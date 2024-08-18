import sys
input=sys.stdin.readline

n=int(input())
a=[]
stack=[]
answer=[]
idx=1
flag=True
for i in range(n):
    tmp=int(input())
    while idx<=tmp:
        stack.append(idx)
        answer.append('+')
        idx+=1
    if stack[-1]==tmp:
        stack.pop()
        answer.append('-')
    else:
        flag=False
        break
if flag:
    for ans in answer:
        print(ans)
else:
    print("NO")