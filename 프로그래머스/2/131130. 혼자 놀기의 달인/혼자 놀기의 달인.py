def solution(cards):
    answer = []
    visit=[0]*(len(cards)+1)
    for card in cards:
        tmp=1
        if not visit[card]:
            x=card
            visit[x]=1
            while True:
                x=cards[x-1]
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