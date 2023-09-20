import sys
input=sys.stdin.readline
n, k=map(int, input().split())
if k<5:
    print(0)
    exit()
elif k ==26:
    print(n)
    exit()
answer =0
def DFS(idx, cnt):
    global answer
    
    if cnt == k-5:
        readcnt=0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    check=False
                    break
            if check:
                readcnt+=1
        answer=max(answer, readcnt)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i]=True
            DFS(i, cnt+1)
            learn[i]=False

words=[set(input().rstrip()) for _ in range(n)]
learn=[0]*26
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c)-ord('a')]=1
DFS(0,0)    
print(answer)