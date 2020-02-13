
class Screen:
    pass
class FourCal:
    def __init__(self):
        print("init")
        self.result = 0 #직전 연산결과 저장
        self.screen = Screen() #집합관계
        pass

    def add(self, newOperand):
        self.result += newOperand
        screen = Screen()
        screen.mro # 사용관계 : 필요할때 1회성으로 객체를 만들어 쓰는것
        return self.result 
        pass

    def mul(self, newOperand):
        self.result *= newOperand
        return self.result
        pass
    
    def sub(self, newOperand):
        self.result -= newOperand
        return self.result 

    def div(self, newOperand):
        self.result /= newOperand
        return self.result 
        pass 

    pass
calc1 = FourCal()

import pprint as pp
pp.pprint(dir(calc1))

# FourCal()
# a = FourCal
# print(type(a))
# print(type(FourCal))
# b = FourCal()
# c = a()
# print(type(b))
# print(type(c))


dir()
