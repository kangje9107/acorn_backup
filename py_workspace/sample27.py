#List 내포 안했을 경우 : 효율성 꽝임 append/insert method를 매번 호출하므로
a=[1,2,3,4,5]
b=[]

for element in a :
    b.append(element * 3)
    pass

#List Comprehension (Dict는 안됨 )
listComprehension = [num for num in a]
print("1. list comprehension:",listComprehension)

#tuple comprehension의 결과는 "generator" type의 객체가 생성됨(tuple X)
tupleComprehension = (v for v in a)
print("2. tuple comprehension:", tupleComprehension)
print('\t- type(tupleComprehension):',type(tupleComprehension))

## generator class object의 1회용 예시 
realTuple = tuple(tupleComprehension)
print("\t- realTuple1:",realTuple)

## 2번째 형변환시 generator은 재사용불가 
realTuple2 = tuple(tupleComprehension) 
print("\t- realTuple2:", realTuple2)

#set comprehension 
setComprehension = {v for v in a}
print("3. set comprehension:",setComprehension)