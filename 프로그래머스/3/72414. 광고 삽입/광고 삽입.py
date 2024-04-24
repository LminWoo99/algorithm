def time_split(x):
    start,end=x.split('-')
    a,b,c=start.split(':')
    start=int(a)*3600+int(b)*60+int(c)
    a,b,c=end.split(':')
    end=int(a)*3600+int(b)*60+int(c)
    return start, end
def int2str(time):
    hour = str(time // 3600).zfill(2)
    minute = str(time % 3600 // 60).zfill(2)
    second = str(time % 3600 % 60).zfill(2)
    
    return hour+":"+minute+":"+second
def solution(play_time, adv_time, logs):
    x,y,z=play_time.split(':')
    play_time=int(x)*3600+int(y)*60+int(z)
    x,y,z=adv_time.split(':')
    adv_time=int(x)*3600+int(y)*60+int(z)
    
    dp=[0]*(play_time+1)
    for log in logs:
        start, end= time_split(log)
        dp[start]+=1
        if end==play_time:
            continue
        dp[end]-=1

    for i in range(1, play_time):
        dp[i]+=dp[i-1]
    for i in range(1, play_time):
        dp[i]+=dp[i-1]
    max_value=-1
    answer=0
    for i in range(adv_time-1, play_time):
        temp=dp[i]-dp[i-adv_time]
        if temp>max_value:
            max_value=temp
            answer=i-adv_time+1
    answer=int2str(answer)

    
    
    return answer