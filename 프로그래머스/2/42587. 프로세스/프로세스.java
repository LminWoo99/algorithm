import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<int []> dq=new LinkedList<>();

        for (int i=0; i<priorities.length; i++){
            dq.add(new int[]{priorities[i], i});
        }
        int i = 1; 
        while (!dq.isEmpty()) {
            int[] element = dq.poll(); 
            if (dq.isEmpty()){
                answer = i;
                break;
            }
            if (element[0] >= Collections.max(dq, Comparator.comparingInt(o -> o[0]))[0]) {
                // 가장 큰 우선순위인 경우
                if (element[1] == location) {
                    answer = i;
                    break;
                }
                i++; 
            } else {
                dq.add(element);
            }
        }
        return answer;
    }
    
}