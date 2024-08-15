import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n=nums.length/2;
        System.out.println(n);
        Set<Integer> arr=new HashSet<>();
        for(int num:nums){
            arr.add(num);
        }
        if(arr.size()<n){
            answer=arr.size(); 
        }
        else{
            answer=n;
        }
        return answer;
    }
}