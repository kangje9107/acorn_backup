# sample56.py

# To use python module 'mod1'

# import mod1  # import: 스크립트파일 처음부터 끝까지 수행된다.
# # (why? 수행시켜야 변수, 함수들을 객체로 리턴하여 활용할 수 있음)

# print(__name__)


import mod1 as m1
print(dir(m1))
print(type(m1.Mod1Class))

obj = m1.Mod1Class()
print(obj)
print(m1.Mod1Class.staticField) #module내의 
print(obj.instanceField) #객체로 
print(obj.method1()) # None반환

