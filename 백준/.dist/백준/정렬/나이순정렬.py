n=int(input())
a=[]
for i in range(n):
    x, y=map(str, input().split())
    x=int(x)
    a.append((x,y))

a.sort(key=lambda x:x[0])
for i in a:
    print(i[0], i[1])