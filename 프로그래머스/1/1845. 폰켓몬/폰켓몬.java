import java.util.*;
class Solution {
    public int solution(int[] nums) {
     int answer=0;
    Set<Integer> set=new HashSet<>();
    for(int num:nums){
        set.add(num);
    }
    int tmp=nums.length/2;
    if (tmp<set.size()){
        answer=tmp;
    }
    else{
        answer=set.size();
    }
        return answer;
    }
}