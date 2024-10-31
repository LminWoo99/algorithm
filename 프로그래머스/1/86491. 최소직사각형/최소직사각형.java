import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max = Arrays.asList(sizes).stream()
                .flatMapToInt(Arrays::stream)
                .max()
                .orElse(0); 
        int b=0;
        for (int [] size : sizes){
            b=Math.max(Math.min(size[0],size[1]), b);
        }
        return max*b;
    }
}