def solution(cards):
    answer = []
    ## 선택할 수 있는 경우의수가 뭐가있지
    ## 일단 사이클이 생기면 안됨
    visit=[0]*(len(cards)+1)
    a=[]
    for idx,val in enumerate(cards):
        a.append([val, idx])
    for val,idx in a:
        tmp=1
        if not visit[val]:
            x=val
            # x_idx=idx
            visit[x]=1
            while True:
                x=a[x-1][0]
                if visit[x]:
                    break
                visit[x]=1
                tmp+=1
            answer.append(tmp)
    if len(answer)>1:
        answer.sort(reverse=True)
        res=answer[0]*answer[1]
    else:
        res=0
    return res