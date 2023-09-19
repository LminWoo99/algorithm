class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return (x-y)
    def multi(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y

class CalculatorProxy:
    def __init__(self):
        self.calculator = Calculator()
    def add(self,x,y):
        return self.calculator.add(x,y)
    def subtract(self,x,y):
        return self.calculator.subtract(x,y)
    def multi(self,x,y):
        return self.calculator.multi(x,y)
    def div(self,x,y):
        return self.calculator.div(x,y)

x,y=map(int,input('정수 두개를 입력하세요. ').split())
proxy = CalculatorProxy()
result=proxy.add(x,y)
print('덧셈 결과:',result)
result=proxy.subtract(x,y)
print('뺄셈 결과:',result)
result=proxy.multi(x,y)
print('곱셈 결과:',result)
result=proxy.div(x,y)
print('나눗셈 결과:',result)
