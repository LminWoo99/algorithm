import java.util.*;
import java.util.Map.Entry;
class Solution {
    public String solution(String[] participant, String[] completion) {
        // List<String> list = new ArrayList<>(Arrays.asList(participant));
        
        String answer="";
        HashMap<String, Integer> dict=new HashMap<>();
        for (String temp:participant){
            if (!dict.containsKey(temp)){
                dict.put(temp, 1);
            }
            else{
                int tmp=dict.get(temp);
                dict.remove(temp);
                dict.put(temp, tmp+1);
            }    
        }
        for (String name: completion){
            int tmp=dict.get(name);
            dict.remove(name);
            dict.put(name, tmp-1);
        }
        for (Entry<String, Integer> entry: dict.entrySet()){
            if (entry.getValue()!=0){
                answer=entry.getKey();
                break;
            }
        }
        
        return answer;
    }
}