def solution(book_time):
    answer = 0
    for i in range(len(book_time)):
        start, end= book_time[i][0], book_time[i][1]
        book_time[i][0], book_time[i][1]= int(start[0:2])*60+int(start[3:]), int(end[0:2])*60+int(end[3:])

    book_time.sort(key=lambda x:(x[0], x[1]))
    room=[]
    for start, end in book_time:
        if len(room)==0:
            answer+=1
            room.append(end)
        else:
            flag=False
            for j in range(len(room)):
                if room[j]+10<=start:
                    room[j]=end
                    flag=True
                    break
            if not flag:
                answer+=1
                room.append(end)
    return answer