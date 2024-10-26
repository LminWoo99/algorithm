import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack=new Stack<>();
        for (int i=0; i<s.length(); i++){
            char a=s.charAt(i);
            if (a=='('){
                stack.push(a);
            }
            else{
                 if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    stack.push(a);  // 짝이 맞지 않으면 스택에 추가하여 불균형을 표시
                }
            }
        }
        if (stack.size()>0){
            answer=false;
        }
        else{
            answer=true;
        }
            
        return answer;
    }
}