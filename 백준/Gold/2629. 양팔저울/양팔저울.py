import sys
input=sys.stdin.readline

cnt=int(input())# 추의 갯수
weight=list(map(int, input().split())) # 추의 무게
check_cnt=int(input()) # 확인하고자 하는 구슬의 개수
res_weight=list(map(int, input().split())) #확인하고자 하는 구슬들
dp=[[0]*(30*500+1) for _ in range(cnt+1)]
res=set()
def cal(left, right, L):
    tmp=abs(left-right)
    if tmp not in res:
        res.add(tmp)
    if L==cnt:
        return 0
    if dp[L][tmp]==0:
        dp[L][tmp]=1
        cal(left+weight[L], right, L+1)
        cal(left, right+weight[L], L+1)
        cal(left, right, L+1)

cal(0,0,0)
for result in res_weight:
    if result not in res:
        print("N", end=" ")
    else:
        print("Y", end=" ")