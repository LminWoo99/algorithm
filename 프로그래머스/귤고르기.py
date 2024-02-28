from collections import Counter
import heapq

def solution(k, tangerine):
    answer = 0
    a=dict(Counter(tangerine))
    hq=[]
    for x,y in a.items():
        heapq.heappush(hq, -y)
    cnt=0
    while hq:
        print(hq)
        y=heapq.heappop(hq)
        answer+=1
        cnt+=-y
        print(cnt)
        if cnt>=k:
            break
    return answer
# 
from collections import Counter

def solution(k, tangerine):
    answer = 0
    a=Counter(tangerine)
    for i in sorted(a.values(),reverse=True):
        k-=i
        answer+=1
        if k<=0:
            break
    return answer
    

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))