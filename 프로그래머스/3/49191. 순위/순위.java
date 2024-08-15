import java.util.*;
class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] graph=new int[n+1][n+1];
        for(int[] edge: results){
            graph[edge[0]][edge[1]]=1;
            graph[edge[1]][edge[0]]=-1;
        }
        for(int i=1; i<n+1; i++){
            for(int j=1; j<n+1; j++){
                for (int k=1; k<n+1; k++){
                    if (graph[i][k]==1&&graph[k][j]==1){
                        graph[i][j]=1;
                        graph[j][i]=-1;
                    }
                    if (graph[i][k]==-1&&graph[k][j]==-1){
                        graph[i][j]=-1;
                        graph[j][i]=1;
                    }
                }
            }
        }
        for(int i=1; i<n+1; i++){
            int cnt=0;
            for (int j=1; j<n+1; j++){
                if (graph[i][j]!=0){
                    cnt++;
                }
            }
            if (cnt==n-1){
                answer+=1;
            }
        }
        return answer;
        
    }
}