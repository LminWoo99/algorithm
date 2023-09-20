n=int(input())
res=[]
for i in range(n):
    a, b=map(int, input().split())
    res.append((a,b))
res.sort(key=lambda x: (x[1], x[0]))
for i in range(len(res)):
    print(res[i][0], res[i][1])