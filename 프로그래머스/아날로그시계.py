def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
#     1초 기준 초침 움직임
    while True:
        h1_position=h1
        if h1>11:
            h1_position=(h1-12)
        if h1==h2 and m1==m2 and s1==s2:
            break
        if m1!=59:
            if s1==m1 and s1/5==h1_position:
                print(m1, h1)
                answer+=1
        s1+=1 
        if s1==60:
            s1=0
            m1+=1
        if m1==60:
            m1=0
            h1+=1
       
    
    return answer

# 시침은 1시간 마다 1칸 1분마다 1/60칸 1초마다 1/3600칸
# 분침은 1분마다 1/5칸 1초마다 1/300
# 시침은 1초만다 1칸
print(solution(11, 59, 30, 12, 0, 0))