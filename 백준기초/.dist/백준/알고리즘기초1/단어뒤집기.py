n=int(input())

for i in range(n):
    res=[]
    a=input()
    b=a.split()
    for j in b:
       res.append(j[::-1])
    for k in res:
        print(k, end=' ')
            

        