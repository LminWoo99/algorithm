import sys
input=sys.stdin.readline
# 피사노 주기
# 주기의 길이가 P 일 때, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같습니다.
# , k > 2 라면, 주기는 항상 15*10**(k-1)

n=int(input())
tmp=1000000
res=[0,1]
p=tmp//10*15
for i in range(2, p):
    res.append(res[i-2]+res[i-1])
    res[i] %=tmp
print(res[n%p])

