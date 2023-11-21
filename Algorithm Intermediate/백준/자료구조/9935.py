import sys
input=sys.stdin.readline

a=input().rstrip()

bomb=input().rstrip()
stack=[]

count=len(bomb)
for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-count:]) == bomb:
        for _ in range(count):
            stack.pop()
    
if stack:
    print(''.join(stack))
    
else:
    print("FRULA")
    