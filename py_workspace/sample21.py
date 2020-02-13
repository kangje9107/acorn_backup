#input() : 내장함수 , 사용자가 입력한 값을 문자열로 가져옴

menu = '''
=======================
        MENU
=======================
1. Add
2. Del
3. List
4. Quit

Enter number :'''

# menu를 출력하면서 prompt를 ':' 바로 옆에 두고 싶으면 ? 
# print 함수 이용시 : end라는 method default 가 \n이므로, 이것을 공백으로 바꿔주어야만 함 
# input() 함수의 전달인자로 menu를 넣으면 \n 가 없어서 바로됨

inputNumber = 0 

while (inputNumber != 4): 
    
    #print(menu, end= '')
    inputNumber = int(input(menu)) 
    print('\t - Input Number :', inputNumber )
    break

