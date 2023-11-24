def solution(alp, cop, problems):
    alp_max=max(map(lambda x: x[0], problems))
    cop_max=max(map(lambda x: x[1], problems))
    dp = [[100000] * (alp_max+1) for _ in range(cop_max+1)]
    alp = min(alp, alp_max) 
    cop = min(cop, cop_max)

    
    dp[alp][cop] = 0
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            if i<alp_max:
                dp[i+1][j]=min(dp[i+1][j], dp[i][j]+1)
            if j<cop_max:
                dp[i][j+1]=min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>= alp_req and j>=cop_req:
                    new_alp=min(alp_max, i+alp_rwd)
                    new_cop=min(cop_max, i+cop_rwd)
                    dp[new_alp][new_cop]=min(dp[new_alp][new_cop], dp[i][j]+cost)
        

    answer=dp[alp_max][cop_max]
    return answer
alp,cop=10,10
problems=[[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp,cop,problems))
