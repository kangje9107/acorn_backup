#-----------------------------------------
#Assignment 5
#-----------------------------------------
# Author: Seungjin
# Date : 2019.12.3
# Subject : Assignment 5
# 함수의 성질을 이용한 커피자판기 만들기


# input(menu, money)
# print(coffee Menu)
# print(change) # 거스름돈 동전 500 100 50 10

# ================ Algorithm ================ #
# 99는 quit
# 없는 번호를 선택하면 오류 표시하고 다시 menu
# 메뉴를 고르면 선택한 메뉴와 함께 가격을 보여줌
# 돈을 받는다
# 돈이 음료값보다 적으면 break
# 돈이 음료값 이상이면 주문한 음료를 주고 잔돈을 준다.

menu = """
===================================
    Welcome to Acorn-bucks
===================================
1. 아메리카노   4,650원
2. 카페라떼     4,940원
3. 카페모카     4,800원
4. 바닐라라떼   5,200원
5. 핫초코       4,500원
6. 자몽티       4,520원
7. 유자차       3,580원
99. 주문취소

음료를 선택해주세요 (번호) : """

def drinks1():
    print('아메리카노를 고르셨습니다.')
    print('아메리카노는 4,650원입니다.')
    cost = 4650
    return cost
    pass

def drinks2():
    print('카페라떼를 고르셨습니다.')
    print('카페라떼는 4,940원입니다.')
    cost = 4940
    return cost
    pass

def drinks3():
    print('카페모카를 고르셨습니다.')
    print('카페모카는 4,800원입니다.')
    cost = 4800
    return cost
    pass

def drinks4():
    print('바닐라라떼를 고르셨습니다.')
    print('바닐라라떼는 5,200원입니다.')
    cost = 5200
    return cost
    pass

def drinks5():
    print('핫초코를 고르셨습니다.')
    print('핫초코는 4,500원입니다.')
    cost = 4500
    return cost
    pass

def drinks6():
    print('자몽티를 고르셨습니다.')
    print('자몽티는 4,520원입니다.')
    cost = 4520
    return cost
    pass

def drinks7():
    print('유자차를 고르셨습니다.')
    print('유자차는 3,580원입니다.')
    cost = 3580
    return cost
    pass  

switch = {  #dictionary
    1: drinks1,
    2: drinks2,
    3: drinks3,
    4: drinks4,
    5: drinks5,
    6: drinks6,
    7: drinks7
}

while 1:
    number = int(input(menu))
    if (number == 99):
        print('주문이 취소되었습니다. \n안녕히가세요!')
        break
        pass

    elif number > 7:
        print('잘못 선택하셨습니다.')
        continue
        pass       

    cost = switch[number]()#dict는 index를 사용할 수 없음. []안의 값은 key임
    money = int(input("\n돈을 넣어 주세요: "))
    if money < cost:
        print("\n돈이 모자랍니다. 돈이 반환됩니다.")
        break
        pass
    else:
        print("\n음료가 준비되었습니다.")
        rmdr = money - cost

        if rmdr > 999 :
            print('거스름돈은 {},{}원입니다.'.format(rmdr//1000,rmdr%1000))
            pass
        else :    
            print('거스름돈은 {}원입니다.'.format(rmdr))
            pass
        
        #잔돈 구하기
        no_500   = rmdr // 500
        rmdr_500 = rmdr % 500
        no_100   = rmdr_500 // 100
        rmdr_100 = rmdr_500 % 100
        no_50    = rmdr_100 // 50
        rmdr_50  = rmdr_100 % 50
        no_10    = rmdr_50 // 10
        rmdr_10  = rmdr_50 % 10

        print(f'반환된 동전은 500원 {no_500}개, 100원 {no_100}개, 50원 {no_50}개, 10원 {no_10}개, 1원 {rmdr_10}개입니다.')





