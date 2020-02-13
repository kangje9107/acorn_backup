class Parent :
    def __init__(self): #Constructor
        print('- Parent::__init__invoked.')
        #super().__init__()
        self.field1 = 0
        pass

    def method1(self): #Method
        print('- parent::method1 invoked.')
        pass

    pass #end class


class Child(Parent):
    def __init__(self):
        print('- Child::__init__invoked.') 
        #super().__init__() #super() 하는 순간, parent class object 생성됨. 부모객체의 속성을 생성 , 초기화해줌  #method chaining
        parent = super() #super class instance 생성
        parent.__init__() 


        # print('\t+ type(super):', type(super))
        # print('\t+ dir(super):', dir(super))
        # print('\t+ type(super()):', type(super))
        # print('\t+ dir(super()):', dir(super))

        pass

    def method2(self):
        print('-Child::method2 invoked')
        pass
    pass

#---------------------------------------------------------#
child = Child()
# print(type(child))
# print(id(child))
# print(dir(child))
# print(child)

print(child.field1) #Child class 안에 super().__init__()안하면 오류남. 
# child.method1()

