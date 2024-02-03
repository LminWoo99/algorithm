
def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1], reverse=True)
    for i in plans:
        i[1]=int(i[1][:2])*60+int(i[1][3:])
    stop=[]
    while len(plans)>=2:
        start=plans[-1][1]
        play=int(plans[-1][2])
        next_start=plans[-2][1]

        spare=next_start-(start+play)
        if spare>=0:
            answer.append(plans[-1][0])
            plans.pop()
            while spare>0 and stop:
                if spare>=stop[-1][1]:
                    spare-=stop[-1][1]
                    answer.append(stop.pop()[0])
                else:
                    stop[-1][1]-=spare
                    break
        else:
            stop.append([plans[-1][0], play-(next_start-start)])
            plans.pop()
    answer.append(plans.pop()[0])
    answer.extend(name for name, play_time in reversed(stop))
                
    return answer
print(solution([["a","09:00","30"],["b","09:10","20"],["c","09:15","20"],["d","09:55","10"],["e","10:50","5"]]))