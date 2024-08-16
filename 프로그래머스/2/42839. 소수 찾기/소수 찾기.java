import java.util.*;
class Solution {
    static Set<Integer> arr=new HashSet<>();
    static int answer=0;
    public int solution(String numbers) {
        boolean[] visit=new boolean[numbers.length()];
        DFS(numbers,visit, numbers.length(), "");
        check();
        return answer;

    }
    public void DFS(String numbers, boolean[] visit, int n, String cnt){
        if (cnt!=""){
            arr.add(Integer.parseInt(cnt));
        }
        for (int i=0; i<n; i++){
            if (visit[i]==false){
                visit[i]=true;
                DFS(numbers, visit, n, cnt+numbers.charAt(i));
                visit[i]=false;
            }
        }

    }
    
    public void check(){

        for (int target : arr){
            boolean flag=true;
            if (target==2){
                answer+=1;
                continue;
            }
            if (target<=1){
                continue;
            }
            for (int i=2; i<(int) Math.sqrt(target)+1; i++){
                if (target%i==0){
                    flag=false;
                    break;
                }
            }
            if (flag){
                answer+=1;
            }
        }
    }
}
