def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        ## 설치
        if b==1:
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
        ## 삭제
        else:
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
    answer.sort(key=lambda x:(x[0],x[1], x[2]))
    return answer
def check(answer):
    for x,y,a in answer:
        # 기둥인 경우
        if a==0:
            # 바닥 x
            # 좌표 아래에 기둥이 존재 x, # 보의 한 쪽 위 x
            if (y!=0 and [x,y-1,0] not in answer and [x-1,y,1] not in answer and [x,y,1] not in answer):
                return False
        # 보인경우
        else:
            if ([x,y-1, 0] not in answer and [x+1, y-1, 0] not in answer and ([x-1,y,1] not in answer or [x+1, y, 1] not in answer)):
                return False
    return True