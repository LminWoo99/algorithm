from collections import deque
from itertools import combinations as c
import sys

input = sys.stdin.readline
INF = 100000 #임의의 큰 수


def bfs(q, blanks):
	visited = [[-1] * n for _ in range(n)]

	time = 0
	while True:
		length = len(q) # 큐의 길이(=1초 동안 새롭게 추가된 바이러스의 수)
		
		if blanks == 0 or length == 0:
			if blanks == 0: # 옵션 1. 모든 빈 칸에 바이러스를 퍼뜨리면 종료
				return time
			else: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
				return INF

		time += 1
		for i in range(length): #큐 길이만큼 반복해주는 for문이 이 문제 해결의 핵심**
			x, y = q.popleft()
			if visited[x][y] == -1:
				visited[x][y] = 1

			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]

				if 0<=nx<n and 0<=ny<n:
					if visited[nx][ny] == -1: #아직 방문하지 않은 칸에 대해
						if board[nx][ny] == 0: # case 1: 빈 칸을 만난 경우
							q.append((nx, ny))
							visited[nx][ny] = 1
							blanks -= 1
						elif board[nx][ny] == 2: # case 2: 비활성된 바이러스를 만난 경우
							q.append((nx, ny))
							visited[nx][ny] = 1

n, m = map(int, input().rstrip('\n').split())
board = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

virus_pos = [] # 바이러스 위치 정보 저장
blank_cnt = 0 # 빈 칸의 개수

# 1. 완전탐색을 통해 빈 칸의 개수를 구하고, 모든 바이러스의 위치 정보 저장 : O(N^2)
for i in range(n):
	for j in range(n):
		if board[i][j] == 0:
			blank_cnt += 1
		
		elif board[i][j] == 2:
			virus_pos.append((i, j))

# BFS를 위한 방향벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
virus_combi = c(virus_pos, m)
res = INF

for virus_list in virus_combi: #모든 조합 결과에 대하여
	q = deque()
	for virus in virus_list:
		q.append(virus)

	tmp = bfs(q, blank_cnt) #BFS 수행
	res = min(res, tmp)

if res == INF: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
	print(-1)
else:
	print(res)