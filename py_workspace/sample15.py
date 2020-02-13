#Dictionary 기본 

#Dict type 선언
dic={}
dic2={1}
 
print(type(dic))
print(type(dic2)) #수학에서의 Set(집합)이 됨
print(id(dic))
print(len(dic))

#Element 삽입
dic = {'name':'Yoseph', 'age':24 }
dic['tel'] = '01012345612'
dic[1] = 99
dic['innerDic'] = {}
dic['innerDic2'] = dict() 

#ELement 변경 
dic['age'] = 18 

#Key는 Unique해야하는데 mutable type을 넣으면 Error
#dic[ [1,2,3] ] = str([1,2,3]) #TypeError: unhashable type: 'list 

#Element 삭제
del dic[1] #해당 key 삭제 
del dic['innerDic']
del dic2
#del dic #해당 Dict 삭제

#Dict[key] = Value 참조
dic3 = {1: 'v1', 2 : 'v2'}
print(dic3[0]) # Indexing 불가. KeyError: 0
print(dic['name'])

#Key 중복시
dic2 = {1: 'value1', 1 : 'value2'}
print(len(dic2)) # 1개만 생성됨

