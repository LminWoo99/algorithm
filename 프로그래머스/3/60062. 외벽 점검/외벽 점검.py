from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    # 0부터 length-1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        for workers in list(permutations(dist, len(dist))):
            count=1
            # 해당 일꾼이 점검할 수 있는 마지막 위치
            position=weak[start]+workers[count-1]
            for idx in range(start, start+length):
                if position<weak[idx]: #새로운 친구 투입
                    count+=1
                    if count>len(dist):
                        break
                    position=weak[idx]+workers[count-1]
            answer=min(answer,count)
    if answer==len(dist)+1:
        return -1
        
    return answer