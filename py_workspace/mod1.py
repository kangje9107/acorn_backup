# Python Module: mod1

# To make a python module.

if(__name__=='__main__'):            #직접 수행시킬 떄는, '___main__'으로 나온다.
    print('The name of "mod1" is', __name__)
    print('---------------------mod1 start ---------------------')
    pass

# 하지만 import해서 모듈로 돌리게되면 __main__으로 나오지 않고, 아무 이름도 안나온다.

def add(num1, num2):
    return num1+num2
    pass

def sub(num1, num2) :
    return num1 - num2
    pass

mulFunc = lambda num1, num2: num1*num2

PI = 3.14159      #원주율


if(__name__=='__main__'):
    print('---------------------mod1 end ---------------------')
    pass




class Mod1Class: 
    staticField =10

    def __init__(self): 
        print('Mod1Calss::Constructor invoked.')

        super().__init__()
        self.instanceField = 20
        pass
    
    def method1(self):
        print('Mod1Class::method1 invoked.')
        pass

