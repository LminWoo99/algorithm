import random
userNum =0
comNum =0

def check(usernum,comnum):
    if usernum == 3:
        tex = '당신 3승!'
        return tex
    elif comnum == 3:
        tex = '컴퓨터 3승!'
        return tex
    else:
        pass
    
while(True):
    user = input('가위, 바위, 보 중 하나를 입력하시오: ')
    if user =='가위' or user=='바위' or user=='보':
        com = random.choice(['가위','바위','보'])
        print('컴퓨터:',com)
        
        if (user=='가위' and com=='보')or(user=='보' and com=='바위')or(user=='바위' and com =='가위'):
            print('당신 승')
            userNum +=1
                
        elif(user==com):
            print('비겼습니다')
                
        else:
            print('컴퓨터 승')
            comNum +=1
        
    else:
        print('입력오류')
    print(check(userNum,comNum))
    
    