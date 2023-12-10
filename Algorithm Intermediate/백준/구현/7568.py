import sys
input=sys.stdin.readline

n=int(input())
info=[]
res=[1]*n
for i in range(n):
    weight, height=map(int, input().split())
    info.append((weight, height))
for i in range(n):
    for j in range(n):
        if i!=j:
            if info[i][0]<info[j][0] and info[i][1]<info[j][1]:
                res[i]+=1
print(*res)