#dict_keys, dict_values, dict_items 내장형 list 객체 (??)
#리스트를 돌려주기 위해서는 메모리 낭비가 발생하는데 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 돌려준다. 
#dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복(iterate) 구문(예: for문)을 실행할 수 있다.

#.keys() : DICT의 KEY값만 dict_keys() 라는 instance로 뽑아냄
dic4 = {'name':'pey', 'phone':'1231241', 'birth':'1118'}
keys = dic4.keys()

print(type(keys))
print(keys)
print(len(keys))

#dict_keys()의 활용: for문. List type method사용 불가
#당장에 메모리에 list로 할당하는게 아니므로 for 문이 아니면 접근할 방법이 없음
for key in keys : 
    print(key)
    pass

#그럼 Key 값을 List 로 뽑아내려면?
list_of_keys = list(dic4.keys())

#.values() : VALUE 만 dict_values instance로 반환
#.clear() (KEY:VALUE) 전체 쌍 삭제 후 빈 {} 남기기
>>> a.clear()
>>> a
{}
 
#.items() (Key:Value)의 튜플들을 dict_items 객체로 돌려줌
allItems = dic4.items()
print(type(allItems))
print(len(allItems))
print(allItems)


for (key,value) in allItems:
    print(key,value)
    pass


#.get(KEY) 함수 & 결측치 처리(통계)
#.get(KEY) Method와 a[KEY]의 차이 : 없는 KEY입력시 Method는 None 반환, a[KEY]는 오류
a = dic4
print(a.get('name'))
print(a.get('asdfgc'))
print(type(a.get('asdfgc'))) #None type

#있는 KEY임에도 값이 None일 수 있어서, None이 반환됬을경우 KEY가없는지 Value인지 구분 불가
a['sno'] = None 

#결측치 처리에 활용
#.get(KEY,default value) : 없는 KEY일 경우, None말고 default value 반환
sno = a.get('sno', '000000-000000')

#DICT안에 특정 KEY가 있는지 T/F로 찾기. VALUE는 못찾음
a = {'name':None, 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print(1118 in a)




