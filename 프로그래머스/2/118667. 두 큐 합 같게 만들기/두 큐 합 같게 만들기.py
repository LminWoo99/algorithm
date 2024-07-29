from collections import deque
def solution(queue1, queue2):
    dq1_sum=sum(queue1)
    dq2_sum=sum(queue2)
    total_len=len(queue1)*3
    queue1, queue2=deque(queue1), deque(queue2)
    ## 두개의 큐 전체합을 먼저 구한다
    answer=0
    while True:
        if answer>=total_len:
            answer=-1
            break
        if dq1_sum==dq2_sum:
            return answer
        if dq1_sum<dq2_sum:
            tmp=queue2.popleft()
            queue1.append(tmp)
            dq1_sum+=tmp
            dq2_sum-=tmp
        else:
            tmp=queue1.popleft()
            queue2.append(tmp)
            dq1_sum-=tmp
            dq2_sum+=tmp
        answer+=1
    return answer