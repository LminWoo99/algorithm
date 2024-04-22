import sys
N = int(sys.stdin.readline())
words = list(sys.stdin.readline().rstrip())
mv = float('-inf')

def DFS(i, value):
    global mv
    if i==N:
        mv=max(mv, int(value))
        return
    #괄호 선택 0
    if i+4 <= N:
        DFS(i+4, str(eval(''.join([value, words[i]] + [str(eval(''.join(words[i+1:i+4])))]))))
    # 괄호 사용 x
    if i+2 <= N:
        DFS(i+2, str(eval(''.join([value] + words[i:i+2]))))

DFS(1, words[0])
print(mv)