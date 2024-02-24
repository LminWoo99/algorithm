import heapq
def solution(n, k, enemy):
    answer = 0
    hq=[]
    temp=0
    for i in enemy:
        heapq.heappush(hq, -i)          
        temp+=i
        if temp>n:
            if k==0:
                break
            temp+=heapq.heappop(hq)
            k-=1
        answer+=1
            
    return answer