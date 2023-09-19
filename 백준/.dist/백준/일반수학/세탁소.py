change=[25, 10, 5, 1]
n=int(input())
for i in range(n):
    a=int(input())
    res=[0]*4
    for j in range(4):
        if a>=change[j]:
            res[j]=(a//change[j])
            a=a%change[j]
        print(res[j], end=' ')