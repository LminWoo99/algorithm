import sys
input=sys.stdin.readline

a=input().rstrip()
bomb=input().rstrip()
tmp=len(bomb)
stack=[]
for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-tmp:])==bomb:
        for j in range(tmp):
            stack.pop()
if ''.join(stack):
    print(''.join(stack))
else:
    print("FRULA")