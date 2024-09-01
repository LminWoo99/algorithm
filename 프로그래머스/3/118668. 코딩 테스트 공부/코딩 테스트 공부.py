def solution(alp, cop, problems):
    ## 일단 문제의 최댓값 알고력, 해결력을 구함
    alp_max=max(map(lambda x: x[0], problems))
    cop_max=max(map(lambda x: x[1], problems))
    dp = [[100000] * (cop_max+1) for _ in range(alp_max+1)]
    alp = min(alp, alp_max) 
    cop = min(cop, cop_max)
    answer=0
    
    dp[alp][cop] = 0
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            if i<alp_max:
                dp[i+1][j]=min(dp[i+1][j], dp[i][j]+1)
            if j<cop_max:
                dp[i][j+1]=min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>=alp_req and j>=cop_req:
                    new_x=min(alp_max, i+alp_rwd)
                    new_y=min(cop_max, j+cop_rwd)
                    dp[new_x][new_y]=min(dp[i][j]+cost, dp[new_x][new_y])
    answer=dp[alp_max][cop_max]
    return answer