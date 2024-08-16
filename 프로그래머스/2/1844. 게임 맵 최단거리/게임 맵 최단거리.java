import java.util.*;
class Solution {
    int[] dx={-1,0,1,0};
    int[] dy={0,1,0,-1};
    public int solution(int[][] maps) {
        int answer = 0;
        int n=maps.length;
        int m=maps[0].length;
        answer=BFS(maps, 0,0,n,m);
        return answer;
    }
    public int BFS(int[][] maps, int x,int y, int n, int m){
        Queue<List<Integer>> dq=new LinkedList<>();
        dq.add(List.of(x,y,1));
        int[][] visit=new int[n][m];
        visit[x][y]=1;
        while(!dq.isEmpty()){
            List<Integer> arr=dq.poll();
            int tmp_x=arr.get(0);
            int tmp_y=arr.get(1);
            int cnt=arr.get(2);
            if (tmp_x==n-1 && tmp_y==m-1){
                return cnt;
            }
            for (int i=0; i<4; i++){
                int xx=tmp_x+dx[i];
                int yy=tmp_y+dy[i];
                if (xx >= 0 && xx < n && yy >= 0 && yy < m && maps[xx][yy]==1 && visit[xx][yy]==0){
                    visit[xx][yy]=1;
                    dq.add(List.of(xx,yy, cnt+1));
                }
            }
        }
        return -1;
    }
}