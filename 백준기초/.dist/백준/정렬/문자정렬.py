n=int(input())
a=[]
for i in range(n):
    tmp=input()
    a.append(tmp)
a=set(a)
a=list(a)
a.sort()
a.sort(key=lambda x:len(x))
for i in a:
    print(i)