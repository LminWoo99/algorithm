import sys
input=sys.stdin.readline
def check(a):
    max_cnt=1
    for i in range(n):
        cnt=1
        for j in range(1, n):
            if a[i][j] == a[i][j-1]:
                cnt+=1
            else:
                cnt=1
            max_cnt=max(max_cnt, cnt)
        cnt=1
        for j in range(1, n):
            if a[i][j]==a[i-1][j]:
                cnt+=1
            else:
                cnt = 1
            max_cnt=max(max_cnt, cnt)
    return max_cnt
n=int(input())
a=[list(input().rstrip()) for _ in range(n)]
ans=0

for i in range(n):
    for j in range(n):
        if j+1 <n:
            a[i][j], a[i][j+1]=a[i][j+1], a[i][j]
            cnt=check(a)
            ans=max(cnt, ans)
            a[i][j], a[i][j+1]=a[i][j+1], a[i][j]
        if i+1 < n:
            a[i][j], a[i+1][j]=a[i+1][j], a[i][j]
            cnt=check(a)
            ans=max(cnt, ans)
            a[i][j], a[i+1][j]=a[i+1][j], a[i][j]
print(ans)
