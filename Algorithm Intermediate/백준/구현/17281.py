from itertools import permutations  
import sys   
input = sys.stdin.readline  
  
  
N = int(input())  
# 최댓값 저장  
cnt = 0  
  
hit_info = [[*map(int, input().split())] for _ in range(N)]  
# 2~9번 타자 순열 만들어주기  
for taja in permutations((range(1 , 9)), 8):  
    # 4번 타자는 0번인덱스 선수 고정이므로 추가해주기  
    taja = list(taja[:3]) + [0] + list(taja[3:])  
  
    # 현재 타자  
    hitter = 0  
    # 이번 이닝 점수  
    result = 0  
    for i in range(N):  
        out = 0  
        base = [0,0,0,0]  
  
        # 3아웃 까지 돌려준다.  
        while out < 3:  
            # 현재 이닝 타자 정보에서 현재 타자 불러와주기  
            hit = hit_info[i][taja[hitter]]  
  
            # 아웃, 1루, 2루, 3루, 홈런 일 때의 조건문 작성  
            if hit == 0:  
                out += 1  
  
            # 안타일 때 3루에 주자가 있다면 +1  
            # 이후 베이스 정보 갱신            
            elif hit == 1:  
                result += base[3]  
                base = [0, 1, base[1], base[2]]  
  
            # 2루타인 경우 2, 3루 주자만큼 +1  
            elif hit == 2:  
                result += base[2] + base[3]  
                base = [0, 0, 1, base[1]]  
  
            elif hit == 3:  
                result += base[1] + base[2] + base[3]  
                base = [0, 0, 0, 1]  
  
            elif hit == 4:  
                result += base[1] + base[2] + base[3] + 1  
                base = [0, 0, 0, 0]  
  
            # 다음 타자 불러오기 위해 +1 해준 후 9로 나눠주면 된다.  
            hitter = (hitter+1) % 9  
  
    if result > cnt:  
        cnt = result  
  
print(cnt)