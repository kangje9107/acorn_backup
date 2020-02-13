# # 과제3
# # 오름차순(내림차순) 정렬

# data = [ 1, 23, 8, 11, 56, 77, 18, 29, 33, 44, 44, 77, 100, 98, 55, 20, 7, 2]

# sorted_data = []

# while data:
#     sorted_data.append(min(data))
#     data.remove(min(data))

# print(sorted_data)

def 오름차순(l):
    for i in range(1, len(l)):

        for j in range(0, len(l)-1):

            if l[j] > l[j+1]: 
                l[j+1], l[j] = l[j], l[j+1]
                pass

        pass

    return l
    pass

# print(오름차순(l))

def 내림차순(l):
    for i in range(1, len(l)):

        for j in range(0, len(l)-1):

            if l[j] < l[j+1]: 
                l[j+1], l[j] = l[j], l[j+1]
                pass

        pass

    return l
    pass

# #평균

# print("=" * 50)

# sum_l = 0

def 평균(l):
    
    sum_l = 0
    
    for i in range(0, len(l)):
        sum_l += l[i]
        pass

    result = sum_l / len(l)
    return result
    pass

# print("평균 :", 평균_result)

#중위수

print("=" * 50)

def 중위수(l):
    middle_num = 0

    if len(l) % 2 == 0 :
        middle_num = (l[int(len(l)/2)-1] + l[int(len(l)/2)]) / 2
        pass
    
    else :
        middle_num = l[int(len(l))/2]
        pass
    
    return middle_num
    pass

# print("중위수 :", 중위수_result)

# #최빈값

# print("=" * 50)

# l = [1, 23, 8, 11, 56, 77, 18, 29, 33, 44, 44, 77, 100, 98, 55, 20, 7, 2]

# a = dict()
# freq = 1

# for i in range(0, len(l)): 
#     for j in range(i+1, len(l)): 
#         if l[i] == l[j] : 
#             freq += 1
#             a[l[i]] = freq
#     freq = 1    

# if len(a) == 0 : 
#     print('최빈값 없음')
# else :
#     print('최빈값 :', tuple(a.keys()))

def 최빈값(l):
    Count = 0
    mode = set()

    for i in set(l):

        if l.count(i) > Count:
            Count = l.count(i)
            pass

        pass

    if Count == 0 or 1:        
        return "최빈값 없음"
        pass
    
    for i in set(l):

        if l.count(i) == Count:
            mode.add(i)
            pass

        pass

    return mode
    pass

def 정렬(l):
    while 1:
        try:
            l = switch1[int(input(정렬메뉴))](l)
            break
            pass

        except:
            print('\n'+"잘못 선택하셨습니다.")
            continue
            pass

        pass

    return l
    pass

# print ('최빈값 :' ,최빈값_result)

switch1 = {
    1 : 오름차순,
    2 : 내림차순
}

switch2 = {
    1 : 정렬 ,
    2 : 평균,
    3 : 중위수,
    4 : 최빈값
}

시작메뉴 = '''
--------------------------------------------------
                     Menu
--------------------------------------------------
                1. 정렬
                2. 평균
                3. 중위수
                4. 최빈값
                0. 종료

        Select number : '''

정렬메뉴 = '''
--------------------------------------------------
                     Menu
--------------------------------------------------
                1. 오름차순
                2. 내림차순
                0. 이전으로

        Select number : '''

while 1:

    l = []
    
    while 1:
        try:
            l_number = int(input('\n'+"계산을 원하는 숫자들을 하나씩 입력해 주십시오. 입력숫자가 없을경우 다음단계로 넘어갑니다. : "))
            pass

        except:
            break
            pass

        if type(l_number) == int :
            l.append(l_number)

            print('\n')
            print(l)
            pass

        print('\n')
        pass
 
    while 1:

        number = int(input(시작메뉴))

        if number not in [0, 1, 2, 3, 4] :
            print ('잘못 선택하셨습니다.'+'\n')
            continue
            pass

        if number == 0:
            break
            pass

        print('\n',switch2[number](l))
        pass
    
    pass