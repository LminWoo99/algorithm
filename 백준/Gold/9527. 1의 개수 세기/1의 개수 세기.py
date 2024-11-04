import sys
input=sys.stdin.readline
def solution(x):
    cnt=0
    bin_x=bin(x)[2:]
    n=len(bin_x)
    for i in range(n):
        if bin_x[i]=='1':
            val=n-i-1
            cnt+=a_sum[val]
            cnt +=(x-2**val+1)
            x=x-2**val
    return cnt
A,B=map(int , input().split())
a_sum=[0 for i in range(60)]
for i in range(1, 60):
    a_sum[i]=2**(i-1)+2*a_sum[i-1]
print(solution(B)-solution(A-1))