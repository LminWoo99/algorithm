def solution(commands):
    answer = []

    board=[["EMPTY"]*50 for _ in range(50)]
    merge_check= [[(i, j) for j in range(50)] for i in range(50)]
    def update(x,y,change):
        xx,yy=merge_check[x-1][y-1]
        board[xx][yy]=change
    def updateAll(changeX, changeY):
        for i in range(50):
            for j in range(50):
                if board[i][j]==changeX:
                    board[i][j]=changeY
    def merge(x,y,xx,yy):
        mergeX1, mergeY1=merge_check[x-1][y-1]
        mergeX2, mergeY2=merge_check[xx-1][yy-1]
        
        if board[mergeX1][mergeY1]=="EMPTY":
            board[mergeX1][mergeY1]=board[mergeX2][mergeY2]
        for i in range(50):
            for j in range(50):
                if merge_check[i][j]==(mergeX2, mergeY2):
                    merge_check[i][j]=(mergeX1, mergeY1)

    def unmerge(x,y):
        r,c=merge_check[x-1][y-1]
        tmp=board[r][c]
        for i in range(50):
            for j in range(50):
                if merge_check[i][j]==(r, c):
                    merge_check[i][j]=(i, j)
                    board[i][j]=="EMPTY"
        board[x-1][y-1]=tmp   
            
    for cmd in  commands:
        cmd=cmd.split(' ')
        if cmd[0]=="UPDATE":
            if cmd[1].isdigit():
                update(int(cmd[1]), int(cmd[2]), cmd[3])
            else:
                updateAll(cmd[1], cmd[2])
        elif cmd[0]=="MERGE":
            if (cmd[1]!=cmd[3] or cmd[2]!=cmd[4]):
                merge(int(cmd[1]),int(cmd[2]),int(cmd[3]),int(cmd[4]))
        elif cmd[0]=="UNMERGE":
            unmerge(int(cmd[1]), int(cmd[2]))
        else:
            x,y=int(cmd[1]), int(cmd[2])
            xx,yy=merge_check[x-1][y-1]

            answer.append(board[xx][yy])


    return answer
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))