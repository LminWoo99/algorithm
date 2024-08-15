class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        
        int n=numbers.length;
        DFS(0, 0, numbers, n, target);
        return answer;
        
    }
    public void DFS(int l, int cnt, int[] numbers,int n,int target){
        if(l==n){
            if (cnt==target){
                answer+=1;    
            }
            return;
            }
        DFS(l+1, cnt+numbers[l], numbers,n,target);
        DFS(l+1, cnt-numbers[l], numbers,n,target);
    }
 
}