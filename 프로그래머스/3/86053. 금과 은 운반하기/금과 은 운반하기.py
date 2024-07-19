# n**2 불가
# 정리 새로운 도시를 만들기 위해서 정해진 금이랑 은을 가져다 놔야함
# 대신 트럭의 용량을 넘으면안되고 각각의 도시는 한정된 자원만 가지고있고 각각의 트럭은 속도가 정해져있음
# 제일 빠른 시간

def solution(a, b, g, s, w, t):
    answer = 4*10**14
    start = 0
    end = 4*10**14
    while start<=end:
        mid=(start+end)//2 # mid는 시간
        gold=0
        silver=0
        add=0
        for i in range(len(t)):
            now_gold=g[i]
            now_silver=s[i]
            now_weight=w[i] # 트럭이 실을수있는 무게
            now_time=t[i]
            cnt=mid//(now_time*2)
            if mid%(now_time*2)>=now_time:
                cnt+=1
            gold+=min(now_gold, cnt*now_weight)
            silver+=min(now_silver, cnt*now_weight)
            add+=min(now_gold+now_silver, cnt*now_weight)
        if a<=gold and b<=silver and (a+b)<=add:
            end=mid-1
            answer=min(answer, mid)
        else:
            start=mid+1
    return answer
