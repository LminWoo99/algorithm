from collections import Counter
def solution(participant, completion):
    answer=""
    participant=Counter(participant)-Counter(completion)
    for name in participant:
        if participant[name]>0:
            answer=name
            break
    return answer
            
