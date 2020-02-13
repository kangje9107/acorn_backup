# sample55.py

class Calculator:
    # 클래스변수(x) ====> 정적 필드(static field)
    # 어느 특정 객체마다 고유하게 값을 가지고 있는 필드가 아니라!!!
    # 이 클래스로부터 생성된 모든 객체에 공통적으로 사용 가능한 공유 필드!!
    manufacturer = 'A'
    count = 0 
    
    def __init__(self):
        super().__init__() #자동입력됨
        #count += 1
        # color 속성 --> 이 클래스에서 생성된 객체의 인스턴스 필드(=객체 변수)
        self.color = 'black'
        pass


    def div(self, num1, num2):
        return num1 / num2
        pass # div

    pass # end - class
calc = Calculator()
divResult = calc.div(5,1)  # 5 / 1
print(Calculator.manufacturer)      # OK  : 클래스에 소속된 정적필드임을 명시하기 위해
print(calc.manufacturer)            # 잘못됨! 동일한 값이 나오더라도


#------------------------------------------#
class SafeCalculator(Calculator):

    # Method Ooverloading???
    # - 파이썬 언어는 지원하지 않음.
    # - 의미: 같은 이름의 메소드를 여러개 정의하는 특징.
    # def div(self, num1, num2, num3):
    #     print(' - div2 invoked.')
    #     pass

    # Method Overriding
    def div(self, num1, num2) :
        if (num2 == 0 ):
            return 0
            pass   #if
        # else:
        return num1 / num2
        #    pass   #else
        pass  #div

    pass   #end class

# calc2 = SafeCalculator()
# divResult = calc2.div(5, 0, 99)
# print(divResult)


