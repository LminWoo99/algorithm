import sys
input=sys.stdin.readline

N,a,b = map(int, input().split())
ans=[]

max_building=max(a,b)
for i in range(1, a):
    ans.append(i)
ans.append(max_building)
for i in range(b-1, 0, -1):
    ans.append(i)
if len(ans)>N:
    print(-1)
else:
    print(ans[0], end=" ")
    tmp=N-len(ans)
    for i in range(tmp):
        print(1, end=" ")
    for i in range(1, len(ans)):
        print(ans[i], end=" ")