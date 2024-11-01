import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        List<List<Integer>> trees = new ArrayList<>();
        
        // 트리 초기화
        for (int i = 0; i <= n; i++) { 
            trees.add(new ArrayList<>());
        }
        
        // 트리 연결 구성
        for (int[] wire : wires) {
            trees.get(wire[0]).add(wire[1]);
            trees.get(wire[1]).add(wire[0]);
        }
        
        // 각 연결을 끊어가며 최소 차이를 구함
        for (int[] wire : wires) {
            // 연결 끊기
            trees.get(wire[0]).remove(Integer.valueOf(wire[1]));
            trees.get(wire[1]).remove(Integer.valueOf(wire[0]));
            
            // 한쪽 전력망의 송전탑 개수 구하기
            int a = BFS(wire[0], trees, n);
            int b = n - a;  // 다른 쪽 전력망의 송전탑 개수
            
            // 두 전력망의 송전탑 개수 차이의 최솟값 계산
            answer = Math.min(answer, Math.abs(a - b));
            
            // 연결 복원
            trees.get(wire[0]).add(wire[1]);
            trees.get(wire[1]).add(wire[0]);
        }
        
        return answer;
    }
    
    public int BFS(int start, List<List<Integer>> trees, int n) {
        Queue<Integer> dq = new LinkedList<>();
        int[] visit = new int[n + 1];
        dq.add(start);
        visit[start] = 1; // 시작 노드를 방문 처리
        int cnt = 1;
        
        while (!dq.isEmpty()) {
            int cur = dq.poll();
            for (int next_cur : trees.get(cur)) {
                if (visit[next_cur] == 0) {
                    visit[next_cur] = 1; // 방문 처리
                    dq.add(next_cur);
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
}
