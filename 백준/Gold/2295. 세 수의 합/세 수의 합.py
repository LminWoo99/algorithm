import sys
input=sys.stdin.readline

n=int(input())
res=[]
for _ in range(n):
    tmp=int(input())
    res.append(tmp)
res.sort()
res_sum=set()
for x in res:
    for y in res:
        res_sum.add(x+y)
answer=0
flag=False
for i in range(n-1 , -1, -1):
    for j in range(i+1):
        if res[i]-res[j] in res_sum:
            answer=res[i]
            flag=True
            break
    if flag:
        break
print(answer)