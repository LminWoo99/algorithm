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
        x=friends[i]
        for j in range(n):
            y=friends[j]
            if x!=y:
                if gift_friend[friends_idx[x]][friends_idx[y]]>gift_friend[friends_idx[y]][friends_idx[x]]:
                    cnt+=1
                elif gift_friend[friends_idx[x]][friends_idx[y]]==gift_friend[friends_idx[y]][friends_idx[x]]:
                    if gift_card[x]>gift_card[y]:
                        cnt+=1
        answer=max(cnt, answer)
        
    
    return answer