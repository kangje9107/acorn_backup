#마음속 숫자 맞추기 input 함수 , 범위 1: 45
import random

prompt = ''' Guess 입력: '''

# menu를 출력하면서 prompt를 ':' 바로 옆에 두고 싶으면 ? 
# print 함수 이용시 : end라는 method default 가 \n이므로, 이것을 공백으로 바꿔주어야만 함 
# input() 함수의 전달인자로 menu를 넣으면 \n 가 없어서 바로됨
print("================================================\n1 ~ 45까지의 정수 중 제 마음속 숫자를 맞춰보세요\n================================================")



rightAnswer = random.randrange(1,46)
inputNumber = None
minNumber = 1
maxNumber = 45  
guessCount = 0

while inputNumber != rightAnswer : 
    guessCount += 1 
    inputNumber = int(float(input(prompt)))

    if inputNumber in range(minNumber,maxNumber):

    
        if inputNumber > rightAnswer  :
            maxNumber = inputNumber
            print(">>> %d번째 guess : 입력하신 숫자는 정답보다 큽니다." %guessCount)

        elif inputNumber < rightAnswer : 
            minNumber = inputNumber 
            print(">>> %d번째 guess : 입력하신 숫자는 정답보다 작습니다."%guessCount)
        elif inputNumber == rightAnswer : 
            print(">>> %d번째 guess : 정답을 맞추셨습니다\n***정답은 %d입니다***"%(guessCount, rightAnswer))
            break
        else : 
            pass

        print(">>> 정답은 %d ~ %d까지의 수 중에 있습니다" % (minNumber, maxNumber))
    else : 
        print(">>> 범위를 잘못 입력했습니다. 정답은 %d ~ %d까지의 수 중에 있습니다" % (minNumber, maxNumber))   
    
    print("\n")