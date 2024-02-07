def solution(sequence):
    answer = 0
    plus=[]    
    n=len(sequence)
    plus_cnt= 1
    for i in range(n):
        plus.append(sequence[i]*plus_cnt)
        plus_cnt*=-1
    dp=[[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0]=min(dp[i-1][0]+plus[i-1], plus[i-1])
        dp[i][1]=max(dp[i-1][1]+plus[i-1], plus[i-1])
    max_cnt=max(map(max, dp))
    min_cnt=min(map(min, dp))
    answer=max(abs(max_cnt), abs(min_cnt))
    
    return answer

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))