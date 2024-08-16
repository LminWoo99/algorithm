class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int tmp=brown/2+2;
        for (int i=1; i<tmp/2+1; i++){
            if ((i-2)*(tmp-i-2)==yellow){
                answer[0]=Math.max(i, tmp-i);
                answer[1]=Math.min(i, tmp-i);
                break;
            }
        }
        return answer;
        
        //방정식
        //4-brown=-2(x+y) 구해놓고
        //1,2,3, 증가하면 yellow값 맞는지
    }
}
