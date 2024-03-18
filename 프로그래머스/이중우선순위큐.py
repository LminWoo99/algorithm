import heapq
def solution(operations):
    answer = []
    hq=[]
    for oper in operations:
        x,y=oper.split(' ')
        y=int(y)
        if x=='I':
            heapq.heappush(hq, y)
        elif x=='D':
            if y==1:
                if hq:
                    hq=heapq.nlargest(len(hq), hq)[1:]
            else:
                 if hq:
                    hq=heapq.nsmallest(len(hq), hq)[1:]
    if hq:
        answer=[max(hq), min(hq)]
    else:
        answer=[0,0]
        
    return answer