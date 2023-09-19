from collections import deque
n,k=map(int, input().split())
dq=deque()
res=[]
for i in range(1, n+1):
    dq.append(i)
x=1

while True:
    if dq:
        if x==k:
            res.append(dq.popleft())
            x=1
        else:
            a=dq.popleft()
            dq.append(a)
            x+=1
    else:
        break
print(str(res).replace('[', '<').replace(']', '>'))