def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작시간과 끝시간을 초단위로 변환
    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2  

    # next기준으로 계산할거니 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if startTime == 0 or startTime == 12 * 3600:
        answer += 1

    while startTime < endTime:
        # 시침 1시간 = 30도 -> 1초에 30/3600도 즉, 1/120도 이동
        # 분침 1분 = 6도 -> 1초에 6/60도 즉, 1/10도 이동
        # 초침 1초 = 6도 -> 1초에 6도 이동 
        hCurAngle = startTime / 120 % 360
        mCurAngle = startTime / 10 % 360
        sCurAngle = startTime * 6 % 360

        # 다음 위치가 360도가 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        # 이동했을 때 지나쳤거나 같아졌는지를 비교하는 것이므로 현재위치는 해줄 필요없음
        hNextAngle = 360 if (startTime + 1) / 120 % 360 == 0 else (startTime + 1) / 120 % 360
        mNextAngle = 360 if (startTime + 1) / 10 % 360 == 0 else (startTime + 1) / 10 % 360
        sNextAngle = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360

        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        # 시침/분침과 동시에 겹쳤을 때 중복카운팅 제외 
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1

        startTime += 1
    
    return answer