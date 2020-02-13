#List 조작
#a.extend([4, 5])는 a += [4, 5]와 동일

#.pop(index) Method : List에서 해당 Index element를 삭제함
a = [1,2,3]
a.pop()
a.pop(1)

#.count(value) Method : 
b = [1,2,3,3,3,3]
b.count(3)

#. extend() Method : ()안의 element를 List에 추가하여 확장
a.extend("C")

# + operator 와 .extend()는 엄밀히 같지않다.
a =[1,2,3]
b = [4,5]
result = a + b #+연산자를 통해 a, b List는 원형을 유지한 채 result라는 새 List 생성

#아래 두 코드의 결과는 같음.
a.extend([4,5]) #List a가 확장됨
a += [4,5] #연산자를 통해 확장해서 a에 넣음 
