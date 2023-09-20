n=int(input())
a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
a=sorted(a)
for i in a:
    print(i)