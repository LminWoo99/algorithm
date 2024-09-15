def solution(record):
    answer = []
    nickname=dict()
    for command in record:
        tmp=command.split(' ')
        if tmp[0]=="Enter":
            nickname[tmp[1]]=tmp[2]
        elif tmp[0]=="Change":
            nickname[tmp[1]]=tmp[2]
    for command in record:
        tmp=command.split(' ')
        if tmp[0]=="Enter":
            answer.append(nickname[tmp[1]]+"님이 들어왔습니다.")
        elif tmp[0]=="Leave":
            answer.append(nickname[tmp[1]]+"님이 나갔습니다.")
    return answer