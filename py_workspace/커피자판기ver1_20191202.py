# sample40.py
cashInput = 0 
numberInput = 0
result2 = 0

prompt = '''
    -----------------------------
                MENU
    -----------------------------
    1. Americano : 3,000 won 
    2. Cafe Latte : 3,800 won
    3. Cold Brew : 3,500 won
    4. Cafe Mocha : 4,000 won
    5. Cappucino : 4,000 won
    99. Quit (잔돈 반환)

    Select a number : '''



#돈(지폐 가능)과 메뉴를input받고 
#고른 다양한 커피를출력, 잔돈을 계산
#단 잔돈은 지폐or 동전. 거스름돈은 동전짜리로만 줄 수 있음. 500원짜리100개 10원, 50원 
#------------------------------------------#
# To define the required functions
#------------------------------------------#
def receiveMoney(price):
    coins = [500,100,10] 
    change = 0
    moneyReturn = []
    while 1:
        try : 
            cashInput = int(float(input(">>> {}원을 투입해주세요.\n>>> 99. 잔돈반환\n".format(price))))
            if (cashInput % 10 != 0) : #1원은 안받으려고.
                raise ValueError
                pass 
        except ValueError  :
            print(">>> 잘못투입하셨습니다. 원화 동전/지폐만 투입 가능합니다.") 
            continue
            pass

        if (cashInput == 99): 
            return 99
            pass
        elif (cashInput >= price):

            change = cashInput-price 
            print(">>> 잔돈 {}원이 반환됩니다: ".format(cashInput-price))
            for i in coins : 
                if (change//i > 0): 
                    print(">>> {}원 x {}개".format(i, change//i))
                    change = change - (change//i) * i
                    moneyReturn = {i:change//i}
                    continue
                    pass
                pass
            

            break # while
        pass 

def americano():
    result = 0 
    result = receiveMoney(3000)
    if result == 99 : 
        return 99
        pass 
    else : 
        print(">>> 커피 나오는 곳에서 americano를 받아가세요.")
        return 1
        pass


def cafelatte():
    result = 0 
    result = receiveMoney(3800)
    if result == 99 : 
        return 99
        pass 
    else : 
        print(">>> 커피 나오는 곳에서 cafelatte를 받아가세요.")
        return 1
        pass

def coldbrew():
    result = 0 
    result = receiveMoney(3500)
    if result == 99 : 
        return 99
        pass 
    else : 
        print(">>> 커피 나오는 곳에서 coldbrew를 받아가세요.")
        return 1
        pass

def cafemocha():
    result = 0 
    result = receiveMoney(4000)
    if result == 99 : 
        return 99
        pass 
    else : 
        print(">>> 커피 나오는 곳에서 americano를 받아가세요.")
        return 1
        pass

def cappucino():
    result = 0 
    result = receiveMoney(4000)
    if result == 99 : 
        return 99
        pass 
    else : 
        print(">>> 커피 나오는 곳에서 americano를 받아가세요.")
        return 1
        pass


#--------------------------------------------#
# 파이썬에서, 함수객체는 1급객체(First-Class Object)
#--------------------------------------------#
switch = {
    1: americano,
    2: cafelatte,
    3: coldbrew,
    4: cafemocha,
    5: cappucino,

} # Dictionary (key:value)

while 1:

    try : 
        inputNumber = int(float(input(prompt)))
    except ValueError : 
        print(">>> 잘못입력하셨습니다. Menu의 원하는 숫자를 입력하세요") 
        continue
        pass 

    if(inputNumber == 99):
        print(">>> 안녕히가세요") 
        break
        pass # if
    elif(inputNumber in range(1,len(switch)+1)):
        result2 = switch[inputNumber]()  # 딕셔너리에 저장된 해당번호의 함수호출
        if (result2 == 99) or (result2 == 1) : 
            break
            pass
        pass
    else: 
        print(">>> 잘못입력하셨습니다.  입력하세요") 
        continue

    pass # while



