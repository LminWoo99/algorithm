import sys
from collections import deque
input=sys.stdin.readline
#조건
#주사위 숫자는 맘대로 조작가능, 100칸을 넘어갈수 없음
#사다리는 숫자는 원래번호보다 이동 칸 번호가 크고, 뱀은 그 반대
def BFS():
    dq=deque([1])
    visited[1]=True
    while dq:
        now=dq.popleft()
        for move in range(1,7):
            check_move=move+now
            if 0< check_move <= 100 and not visited[check_move]:
                if check_move in a.keys():
                    check_move=a[check_move]
                if check_move in snake.keys():
                    check_move=snake[check_move]
                if not visited[check_move]:
                    dq.append(check_move)
                    visited[check_move]=True
                    check[check_move]=check[now]+1



    
n,m =map(int, input().split())
a=dict() # 사다리
snake=dict()
check=[0]*101
visited=[False]*101
for i in range(n):
    x,y=map(int, input().split())
    a[x]=y
for i in range(m):
    x,y=map(int, input().split())
    snake[x]=y
BFS()
print(check[100])