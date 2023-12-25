import sys
from itertools import permutations
input=sys.stdin.readline
N,K=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
p2 = list(map(int,input().split())) # 경희
p3 = list(map(int,input().split())) # 민호
jiwo = [i+1 for i in range(N)] # 지우
 
def DFS(py1, py2, index, win, player):
    global result
    if win[0] == K: 
        result = 1
        return
    if win[1] == K or win[2] == K: 
        return
    if index[0] == N: 
        return
    py3 = 3 - (py1+py2) 
    pv1 = player[py1][index[py1]]-1 
    pv2 = player[py2][index[py2]]-1
    index[py1] += 1 
    index[py2] += 1
    if board[pv1][pv2] == 2 or (board[pv1][pv2] == 1 and py1 > py2):
        win[py1] += 1
        DFS(py1, py3, index, win, player)
    elif board[pv1][pv2] == 0 or (board[pv1][pv2] == 1 and py1 < py2): 
        win[py2] += 1
        DFS(py2, py3, index, win, player)
 
for p1 in permutations(jiwo, N):
    player = [p1,p2,p3] 
    index = [0,0,0] 
    win = [0,0,0] # 지우, 경희, 민호가 각각 몇번 이겼는지
    result = 0 # 지우가 이길수있는지
    DFS(0,1,index,win,player)
    if result == 1:
        print(1)
        break
else:
    print(0)
