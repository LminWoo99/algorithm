def solution(x, y, n):
    answer = 0
    dp=[int(1e9)]*(y+1)
    dp[x]=0
    for i in range(x, y+1):
        if y>=i+n:
            dp[i+n]=min(dp[i+n],dp[i]+1)
        if i*3<=y:
            dp[i*3]=min(dp[i*3], dp[i]+1)
        if i*2<=y:
            dp[i*2]=min(dp[i*2], dp[i]+1)
        
    answer=dp[-1]
    if answer==int(1e9):
        return -1
    else:
        return answer
solution(10,40,30)