def solution(storey):
    i=10
    answer=0
    cnt=0
    if storey>=10:
        while True:
            if storey==0:
                break
            cnt=storey%i
            if cnt>(i//2):
                storey+=(i-cnt)
                answer+=(i-cnt)
                cnt=0
                
            else:
                storey-=cnt
                answer+=cnt
                cnt=0
                
                
        
    return answer