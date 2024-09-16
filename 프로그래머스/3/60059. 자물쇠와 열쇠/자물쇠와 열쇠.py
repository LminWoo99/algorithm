def compare(board,key,x,y,M, N):
    answer = True
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]

    for i in range(N):
        if not answer: break

        for j in range(N):
            if board[i+M][j+M] != 1:
                answer = False
                break
    #  더해진 board에 다시 key 빼기
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

    return answer

def solution(key, lock):

    N, M = len(lock), len(key)

    board = [[0] * (N + 2*M) for _ in range(N + 2*M)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    for i in range(4):
        key = rotate(key)
        for i in range(1, N+M):
            for j in range(1, N+M):
                if compare(board, key, i, j, M, N):
                    return True

    return False


def rotate(key):
    n = len(key)

    rotate_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_key[j][n-i-1] = key[i][j]
    return rotate_key