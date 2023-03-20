n=int(input('[용도] 1: 주택용, 2:공업용, 3:산업용?') )
a=int(input('사용량(kwh)?'))
if n<3:
    if n==1:
        print("용도:{}, 사용량:{:.2f}, 전기요금:{:,.2f}원".format(n, float(a), float(a*88+910)))
    else:
        print("용도:{}, 사용량:{:.2f}, 전기요금:{:,.2f}원".format(n, float(a), float(a*182+1600)))
else:
    print("용도:{}, 사용량:{:.2f}, 전기요금:{:,.2f}원".format(n, float(a), float(a*275+7300)))
    