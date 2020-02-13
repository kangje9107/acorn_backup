import copy 

#모듈 사용 : <import한 모듈명>.<사용하려는 맴버>

a = [1,2,3]
b = copy.copy(a)
b = copy.deepcopy(a)
print(id(a))
print(id(b))


#import 키워드를 쓰면, ~~\\copy.py 스크립트 파일이 module클래스의 객체로 들어옴
#원래는 python script file이지만 이렇게 import 하면 module type 의객체로서 모듈이라고 부른다


[a,b,c]= [1,True, 'Python']
[name, age, height, weight ]= [ 'yoseph', 23, 187, 58 ]

print(name, age, height, weight)