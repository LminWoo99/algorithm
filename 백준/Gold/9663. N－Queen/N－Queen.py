import sys
input = sys.stdin.readline

def DFS(row):
    global res
    if row == n:  # 모든 퀸을 놓았다면 성공
        res += 1
        return
    for i in range(n):
        if not (cols[i] or diag1[row+i] or diag2[row-i+n-1]):
            cols[i]=diag1[row+i]=diag2[row-i+n-1]=1
            DFS(row+1)
            cols[i]=diag1[row+i]=diag2[row-i+n-1]=0

n = int(input())
res = 0
cols = [0] * n             # 열 충돌 여부
diag1 = [0] * (2 * n - 1)  # "/" 방향 대각선 충돌 여부
diag2 = [0] * (2 * n - 1)  # "\" 방향 대각선 충돌 여부

DFS(0)
print(res)