import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        List<String> arr=new ArrayList<>();
        for(String name: phone_book){
            arr.add(name);
        }
        Collections.sort(arr);
        String a="12";
        String b="123";
        for (int i=0; i<arr.size()-1; i++){
            if(arr.get(i+1).startsWith(arr.get(i))){
                answer=false;
                break;
            }
        }
        return answer;
    }

}