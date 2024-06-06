import sys
input=sys.stdin.readline

n=int(input())
student=[]
stack=[]
res=0
for _ in range(n):
    student.append(int(input()))
for height in student:
    while stack and stack[-1][0]<height:
        res+=stack.pop()[1]
    if not stack:
        stack.append((height, 1))
        continue
    if stack[-1][0]==height:
        cnt=stack.pop()[1]
        res+=cnt
        if stack:
            res+=1
        stack.append((height, cnt+1))
    else:
        stack.append((height, 1))            
        res+=1
print(res)