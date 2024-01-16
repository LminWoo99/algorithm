import sys
input=sys.stdin.readline
res = [0] * 10
n = int(input())
point = 1
start = 1
def solution(x,res,point):
    while x > 0:
        res[x % 10] += point
        x //= 10

while start <= n:
    while n % 10 != 9:
        solution(n, res, point)
        n -= 1
    if n < start:
        break
    while start % 10 != 0:
        solution(start, res, point)
        start += 1
    start //= 10
    n //= 10
    for i in range(10):
        res[i] += (n - start + 1) * point
    point *= 10

# 출력부
for i in range(10):
    print(res[i], end=' ')