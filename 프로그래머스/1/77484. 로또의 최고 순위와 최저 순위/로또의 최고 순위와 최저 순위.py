def solution(lottos, win_nums):
    answer = []
    cnt=0
    zero_cnt=0
    min_cnt=0
    for num in lottos:
        if num==0:
            zero_cnt+=1
    for lotto in win_nums:
        if lotto in lottos:
            cnt+=1
            min_cnt+=1
        else:
            if zero_cnt>0:
                cnt+=1
                zero_cnt-=1
            
    if min_cnt:
        min_cnt=7-min_cnt
    else:
        min_cnt=6
    if cnt:
        cnt=6-cnt+1
    else:
        cnt=6
    answer.append(cnt)
    answer.append(min_cnt)
    return answer