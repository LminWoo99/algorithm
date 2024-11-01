import java.util.*;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        PriorityQueue<Integer> pqA=  new PriorityQueue<>();
        PriorityQueue<Integer> pqB=  new PriorityQueue<>();
        for (int i=0; i<A.length; i++){
            pqA.add(-A[i]);
            pqB.add(-B[i]);
        }
        while (!pqA.isEmpty()){
            int cntA=-pqA.poll();
            int cntB=-pqB.poll();
            if (cntA<cntB){
                answer+=1;
            }
            else{
                pqB.add(-cntB);
            }
            
        }
        return answer;
    }
}
