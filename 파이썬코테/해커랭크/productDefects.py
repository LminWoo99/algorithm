import sys
input=sys.stdin.readline
def findLargestSquareSize(samples):
    if len(samples)==1 and len(samples[0])==1:
        return 1
    answer=0
    dp=samples
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if dp[i][j]==1:
                dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                answer=max(answer, dp[i][j])
    return answer
        

samples_rows = int(input().strip())
samples_columns = int(input().strip())
samples = []

for _ in range(samples_rows):
    samples.append(list(map(int, input().rstrip().split())))
result = findLargestSquareSize(samples)
print(result)