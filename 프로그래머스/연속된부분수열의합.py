answer = []
def solution(sequence, k):
    global answer
    n=len(sequence)
    res=1000000
    for i in range(n):
        if sequence[i]==k:
            answer=[i,i]
            return answer
    start,end=0,-1
    tmp=0
    while True:
        if tmp==k:
            if res>end-start:
                res=end-start
                answer=[start,end]
            tmp-=sequence[start]
            start+=1
        elif tmp>k:
            tmp-=sequence[start]
            if start>=n:
                break
            start+=1
        else:
            end+=1
            if end>=n:
                break
            tmp+=sequence[end]
    return answer