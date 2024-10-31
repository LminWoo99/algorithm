import java.util.*;

class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        DFS(0, 0, numbers, target);
        return answer;
    }
    public void DFS(int cnt, int L, int[] numbers, int target){
        if (L==numbers.length){
            if  (cnt==target){
                answer+=1;
            }
            return;
        }
        // int tmp=1;
        // for (int i =0; i<2; i++){
        //     int a=numbers[L]*tmp;
        //     cnt+=a;    
        //     cnt*=-1;
        DFS(cnt+numbers[L], L+1, numbers, target);
        DFS(cnt-numbers[L], L+1, numbers, target);
            
        // }
        
    }
}