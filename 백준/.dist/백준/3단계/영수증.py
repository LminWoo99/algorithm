x=int(input())
n=int(input())
cost=[]
res=0
for i in range(n):
    a,b=map(int, input().split())
    cost.append((a,b))
for i in range(len(cost)):
    res+=cost[i][0]*cost[i][1]
if res==x:
    print("Yes")
else:
    print("No")