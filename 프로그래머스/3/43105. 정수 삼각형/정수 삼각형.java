import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        int[][] dp = new int[501][];
        for (int i=0; i<=500; i++){
            dp[i]=new int[i+1];
        }
        dp[0][0]=triangle[0][0];
        int n=triangle.length;
        for (int i=1; i<n; i++){
            for (int j=0; j<i+1; j++){
                // 맨왼쪽 , 오른쪽, 가운데
                if (j==0){
                    dp[i][j]=dp[i-1][j]+triangle[i][j];
                }
                else if (j==i){
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                }
                else{
                    dp[i][j]=Math.max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j];
                }
            }
        }
        answer=Arrays.stream(dp[n-1]).max().getAsInt();
        
        return answer;
    }
}