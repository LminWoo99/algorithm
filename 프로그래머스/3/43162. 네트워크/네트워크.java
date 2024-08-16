import java.util.*;
class Solution {
    static int[] visit=new int[201];
    public int solution(int n, int[][] computers) {
        int answer = 0;    
        for(int i=0; i<n; i++){
            if (visit[i]==0){
                BFS(i,n,computers);
                answer+=1;
            }
            
        }
        return answer;
    }
    public void BFS(int x,int n, int[][] computers){
        Queue<Integer> dq=new LinkedList<>();
        dq.add(x);
        visit[x]=1;
        while (!dq.isEmpty()){
            int k=dq.poll();
            for(int i=0; i<n; i++){
                if (computers[k][i]==1 && visit[i]==0){
                    visit[i]=1;
                    dq.add(i);
                        
                }
            }
        }
        
    }
}