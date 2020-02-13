#* 금일완료과제(17:00부터, 조별발표) *
#
#   주어진 일련의 숫자를 정렬하시오.
#   - 조건1: 버블정렬 알고리즘 사용
#     반드시 참고할 웹페이지 주소:
#
#     https://terms.naver.com/entry.nhn?docId=2270437&cid=51173&categoryId=51173
#
#   - 조건2: 내림차순/오름차순 모두 가능하게
#
#   1, 23, 8, 11, 56, 77, 18, 29, 33,
#   44, 44, 77, 100, 98, 55, 20, 7, 2
#
#   정렬후, 아래의 특성값을 추출하시오.
#   (1) 평균 (2) 중위수 (3) 최빈값


import statistics as st

numberList = [1, 23, 8, 11, 56, 77, 18, 29, 33, 44, 44, 77, 100, 98, 55, 20, 7, 2]


def bubblesort(list):
    
    lengthOfList = len(list) - 1 
    for n in range(lengthOfList): 
        for element in range(lengthOfList - n):
            if list[element] > list[element + 1]:
                list[element], list[element + 1] = list[element + 1], list[element]
                pass # if
            
            pass # inner for
        pass # outer for
    return list

print('='*90)
print('Unsorted list:', numberList)
print('='*90)
print('Sorted list:', bubblesort(numberList))
print('='*90)

# ====  Average  ====
# Method 1
average = round(st.mean(numberList), 2)
print(f'- Average: {average}')

# Method 2
def average(list):
    sum = 0
    for element in list:
        sum += element
        pass
    return sum / len(list)
    pass

average2 = round(average(numberList), 2)
print('- Average2:', average2)

# Method 3
""" def average3(list):
    return round(sum(list) / len(list), 2)
av3 = average3(numberList) """

average3 = lambda list: round(sum(list) / len(list), 2)

print('- Average3:', average3(numberList))    

print('='*90)

# ===== Median =====
# Method 1
median = int(st.median(numberList))
print(f'- Median: {median}')

# Method 2
def median(list):
    bubblesort(list)
    middle_num = 0

    if len(list) % 2 == 0 :
        middle_num = (list[int(len(list)/2)-1] + list[int(len(list)/2)]) / 2
    
    else :
        middle_num = list[int(len(list))/2]
    
    return middle_num
median2 = int(median(numberList))
print('- Median2:', median2)

print('='*90)

# ===== Mode =====
# Method 1
mode = st.mode(numberList)
print(f'- Mode: {mode}')

# Method 2
def mode(list):
    maxCount = 0
    mode = set()

    for i in set(list):
        if list.count(i) > maxCount:
            maxCount = list.count(i)
        
    for i in set(list):
        if list.count(i) == maxCount:
            mode.add(i)

    return mode

mode2 = mode(numberList)
print('- Mode2:', mode2)




