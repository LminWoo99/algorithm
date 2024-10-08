from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    n=len(friends)
    gift_card=defaultdict(int) ## 선물 지수 카운트
    gift_friend=[[0]*n for _ in range(n)]
    friends_idx=defaultdict(int)
    
    for idx, val in enumerate(friends):
        friends_idx[val]=idx
    for gift in gifts:
        x,y=gift.split(' ')
        if not gift_card[x]:
            gift_card[x]=1
        else:
            gift_card[x]+=1
        if not gift_card[y]:
            gift_card[y]=-1
        else:
            gift_card[y]-=1
        gift_friend[friends_idx[x]][friends_idx[y]]+=1
    for i in range(n):
        cnt=0
        for j in range(n):
            if i!=j:
                if gift_friend[i][j]>gift_friend[j][i]:
                    cnt+=1
                elif gift_friend[i][j]==gift_friend[j][i]:
                    if gift_card[friends[i]]>gift_card[friends[j]]:
                        cnt+=1
        answer=max(cnt, answer)
        
    
    return answer