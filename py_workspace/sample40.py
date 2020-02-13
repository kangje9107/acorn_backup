
print("__name__:",__name__) #python interpretor가 설정한 전역변수, 현재 python module의 이름을 나타냄 
#현재 수행중인 python module 의 이름을 __main__으로 정해놓음.(imported module 제외)

class Calculater : 
    def __init__(self, color, shape, material): #생성된 객체(empty) 주소를 다시 self 넣어줌.  
        print('- Calcutlator::__init__invoked.')
        print('\t + self:',self)

        #색상필드
        self.color = color #변수.field명 : field(객체의 속성) 생성
        self.shape = shape
        self.material = material
        pass # Constructor

    def wriggle(self):
        print('- Calcutlator::wriggle invoked.')
        print("%s색의 전자계산기가 꿈틀거립니다." % self.color)
        return False
        pass

    def say_hello(self):
        print('- Calcutlator::say_hello invoked.')
        self.wriggle()
        #self.wriggle(self) #오류발생
        self.weight = 50
        pass
    pass

#A회사
calc1 = Calculater("Black", "Triangle", "plastic")
print("\t + calc1:", calc1)
print('\t\t++ calc1.color:',calc1.color)
print('\t\t++ calc1.shape:',calc1.shape)
print('\t\t++ calc1.material:',calc1.material)


result = calc1.wriggle()
print('- result:', result)


calc1.say_hello()

print('\t\t++ calc1.weight:',calc1.weight)

calc1.size = 4 #class밖에서 속성값을 설정하지마라   
