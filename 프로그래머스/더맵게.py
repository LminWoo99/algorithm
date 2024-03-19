import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    flag=False
    while scoville:
        first=heapq.heappop(scoville)
        if first>=K:
            flag=True
            break
        if not len(scoville):
            break
        second=heapq.heappop(scoville)
        answer+=1
        heapq.heappush(scoville, first+(second*2))
    if flag:
        return answer
    else:
        return -1