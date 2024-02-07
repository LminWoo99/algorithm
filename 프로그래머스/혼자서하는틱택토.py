# BFS 풀이
# from collections import deque
# dx=[-1,0,1,0, 1, 1, -1, -1]
# dy=[0,1,0,-1,1, -1,-1,1]
# def solution(board):
#     answer = 1
#     o_cnt=sum(row.count('O') for row in board)
#     x_cnt=sum(row.count('X') for row in board)
#     def finish(x,y,state):
#         dq=deque()
#         dq.append((x,y,1))
#         visit=[[0]*3 for _ in range(3)]
#         visit[x][y]=1
#         while dq:
#             x,y,cnt=dq.popleft()
#             if cnt>=3 and state=='O':
#                 if o_cnt-1!=x_cnt:
#                     return 0
#             if cnt>=3 and state=='X':
#                 if o_cnt!=x_cnt:
#                     return 0
#             for i in range(8):
#                 xx,yy=x+dx[i], y+dy[i]
#                 if 0<=xx<3 and 0<=yy<3 and visit[xx][yy]==0 and board[xx][yy]==state:
#                     visit[xx][yy]=1
#                     cnt+=1
#                     xx,yy=xx+dx[i], yy+dy[i]
#                     if 0<=xx<3 and 0<=yy<3 and visit[xx][yy]==0 and board[xx][yy]==state:
#                         visit[xx][yy]=1
#                         dq.append((xx,yy, cnt+1))
#         return 1
   
#     if x_cnt-o_cnt>0 or abs(x_cnt-o_cnt)>1:
#         return 0
#     else:
#         O=[]
#         X=[]
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j]=='X':
#                     X.append((i,j))
#                 if board[i][j]=='O':
#                     O.append((i,j))
#         for i,j in O:
#             answer=finish(i,j, 'O')
#             if not answer:
#                 return answer
#         for i,j in X:
#             answer=finish(i,j, 'X')
#             if not answer:
#                 return answer
#         return answer
            
        

def check_win(player, board):
    for i in range(3):
        if all(state==player for state in board[i]):
            return True
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)
    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0
    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
        return 0
    return 1