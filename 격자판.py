n=int(input())
#2차원 리스트 입력 받기
a=[list(map(int, input().split())) for _ in range(n)]
lag=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if(sum1>lag):
        lag=sum1
    if(sum2>lag):
        lag=sum2
sum1=sum2=0
for i in range(n):
        sum1+=a[i][i]
        sum2+=a[i][n-i-1]
        if(sum1>lag):
            lag=sum1
        if(sum2>lag):
            lag=sum2
print(lag)