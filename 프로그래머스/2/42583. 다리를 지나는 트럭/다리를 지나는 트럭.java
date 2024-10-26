import java.util.*;
class Solution {
    static int cur_time=0;
    static int sum = 0;
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q=new LinkedList<>();
        int i=0;
        
        for (int truck: truck_weights){
            while (true){
                if (q.isEmpty()){
                    q.add(truck);
                    sum+=truck;
                    cur_time+=1;
                    break;
                }
                else if (bridge_length==q.size()){
                    sum-=q.poll();
                }
                else{
                    if (sum+truck<=weight){
                        q.add(truck);
                        sum+=truck;
                        cur_time+=1;
                        break;
                    }
                    else{
                        q.add(0);
                        cur_time+=1;
                    }
                }
                
            }
        }
       return cur_time + bridge_length; 
    }
}