def solution(n, tops):
    answer = 0
    MOD=10007
    a=[0]*100001  
    b=[0]*100001
    a[0],b[0]=0,1
    for i in range(1, n+1):
        if tops[i-1]:
            a[i]=(a[i-1]+b[i-1])%MOD
            b[i]=(a[i-1]*2+b[i-1]*3)%MOD
        else:
            a[i]=(a[i-1]+b[i-1])%MOD
            b[i]=(a[i-1]+b[i-1]*2)%MOD
    answer=(a[n]+b[n])%MOD
    return answer