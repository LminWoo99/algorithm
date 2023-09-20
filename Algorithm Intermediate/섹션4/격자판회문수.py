a=[list(map(int, input().split())) for _ in range(7)]
res=0
def check(a):
    res=0
    for i in range(3):
        temp=a[i:i+5]
        temp.reverse()
        if temp==a[i:i+5]:
            res+=1
        else:
            res+=0
    return res
for i in range(7):
    temp=list([0]*7)
    temp2=list([0]*7)
    for j in range(7):
        temp[j]=a[i][j]
        temp2[j]=a[j][i]
    res+=check(temp)
    res+=check(temp2)
print(res)
            