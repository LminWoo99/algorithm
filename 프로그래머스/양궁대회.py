max_gap=0
score=[0]*11
answer = [-1]
def solution(n, info):
    
    def DFS(L, cnt):
        global max_gap
        global answer
        global score
        if L==11 or cnt==0:
            winner, gap=check(score)
            if winner:
                if cnt>=0:
                    score[10]=cnt
                if gap>max_gap:
                    max_gap=gap
                    answer=score.copy()
                elif gap==max_gap:
                    for i in range(len(score)):
                        if answer[i] > 0:
                            max_i_1 = i
                        if score[i] > 0:
                            max_i_2 = i
                    if max_i_2 > max_i_1:
                        answer = score.copy()
            return
        if cnt>info[L]:
            score[L]=info[L]+1
            DFS(L+1, cnt-score[L])
            score[L]=0
        DFS(L+1, cnt)
        
    def check(score):
        a,b=0,0
        for i in range(len(info)):
            if info[i]>score[i]:
                a+=(10-i)
            elif info[i]<score[i]:
                b+=(10-i)
        return (b>a , abs(a-b))
    DFS(0,n)
    

    return answer