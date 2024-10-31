import java.util.*;
class Solution {
    static Set<Integer> res=new HashSet<>();
    static boolean[] visited;
    public int solution(String numbers) {
        // ## DFS로 만들 수 있는 수를 모두 구하고 소수구하기
        int n=numbers.length();
        visited=new boolean[n];
        DFS(numbers, "", n);
        return isPrime();

    }
    public void DFS(String numbers, String number, int n){
        if (number!=""){
            res.add(Integer.valueOf(number));
        }
        for (int i=0; i<n; i++){
            if (visited[i]==false){
                visited[i]=true;

                DFS(numbers, number+numbers.charAt(i), n);
                visited[i]=false;
            }
        }    
    }
    public int isPrime(){
        int cnt=0;

        for (int target : res){
            if (target<2){
                continue;
            }
            boolean flag=true;
            for (int i=2; i<(int)Math.sqrt(target)+1; i++){
                if (target%i==0){
                    flag=false;
                    break;
                }
            }
            if (flag==true){
                cnt+=1;
            }
        }
        return cnt;
    }
}
