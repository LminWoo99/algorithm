import heapq
from itertools import product

def check_time(mento_distribute, k, reqs):
    mento = []
    waiting = 0
    
    for n in mento_distribute:
        mento.append([0 for x in range(n)])
    
    for s, f, num in reqs:
        time = heapq.heappop(mento[num-1])
        print(time)
        waiting += max(0, time-s)
        heapq.heappush(mento[num-1], max(s, time)+f)
   
    return waiting
    
def solution(k, n, reqs):
    answer = float("inf")
    
    for mento_distribute in product(range(1, n+1), repeat=k):
        if sum(mento_distribute)==n:
            answer=min(check_time(mento_distribute, k, reqs),answer)
            
    
    return answer
solution(3,5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])