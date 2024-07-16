import heapq

# 야근 피로도= 남은 일의 작업량을 제곱하여 더한 값
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return answer
    else:
        hq=[]
        for work in works:
            heapq.heappush(hq, -work)
        i=1
        while True:
            if i>n:
                break
            work=heapq.heappop(hq)
            work=(-work-1)
            if work>0:
                heapq.heappush(hq, -work)
            i+=1
        for work in hq:
            answer+=(work**2)
        return answer
        