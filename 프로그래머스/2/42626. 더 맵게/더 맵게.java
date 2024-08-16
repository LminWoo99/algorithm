import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> hq=new PriorityQueue<>();
        for(int i: scoville){
            hq.add(i);
        }
        int min_num=Arrays.stream(scoville).min().getAsInt();
        while (true){
            int first=hq.poll();
            if (first>=K){
                break; 
            }
            answer+=1;
            if (hq.size()==0){
                answer=-1;
                break;
            }
            int second=hq.poll();
            hq.add(first+2*second);            
        }
        return answer;
    }
}
