from collections import deque
def solution(picks, minerals):
    cnt = sum(picks)
    num_min = cnt * 5
    if len(minerals) > num_min: 
        minerals = minerals[:num_min]
    answer = 0
    check=[[0,0,0] for x in range(10)]
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            check[i//5][0]+=1
        elif minerals[i]=="iron":
            check[i//5][1]+=1
        else:
            check[i//5][2]+=1
    check=sorted(check, key=lambda x:(-x[0], -x[1], -x[2]))
    print(check)
    for mineral in check:
        x,y,z = mineral
        for p in range(len(picks)):
            if p==0 and picks[p]>0:
                picks[p]-=1
                answer+=x+y+z
                break
            elif p==1 and picks[p]>0:
                picks[p]-=1
                answer+=5*x +y +z
                break
            elif p==2 and picks[p]>0:
                picks[p]-=1
                answer+= 25*x+ 5*y +z
                break
        
        
    return answer