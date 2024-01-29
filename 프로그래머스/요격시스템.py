def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    
    cnt=0
    for x,y in targets:
        if not x<cnt<y:
            cnt=y-0.1
            answer+=1
        
            
    return answer