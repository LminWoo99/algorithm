def cal(tmp):
    if tmp=='+':
        print('{}+{}={}'.format(num1,num2,int(num1)+int(num2)))
    elif tmp=='-':
        print('{}-{}={}'.format(num1,num2,int(num1)-int(num2)))
    elif tmp=='*':
        print('{}*{}={}'.format(num1,num2,int(num1)*int(num2)))
    else:
        print('{}/{}={}'.format(num1,num2,int(num1)//int(num2)))
num1, n, num2 =map(str, input('숫자1, 부호, 숫자2 : ').split())
print(num1, n, num2)
cal(n)