#Lambda Expression : 익명함수
def add(num1, num2):
    return num1 + num2
    pass

# result = add(1,2)
# print(result)
# print(type(result))
# print(id(result))

# #lambda 변수1, 변수2,..: 표현식(단1개)
# result2 = lambda num1, num2: num1+num2
# print(result2)
# print(result2(1,2))

# #매개변수가 없는 lambda : 가능 
# result3 = lambda : 1 + 2
# print(result3) 

# a = 1
# b = 2
# print(a),print(b) #tuple을 생성하는 구문
# print(a,end="----");print(b) 


result4 = lambda num1, num2: print(num1+num2)

 
result4(1,2)
print(result4) 
print(result4(1,2)) #print()의 return값도 함께 출력됨 

#자동으로 return이적용되므로, return을 적으면 오류 발생
# result4 = lambda num1, num2: return num1+num2

# Lambda 활용 사례 : filter()
# 과제 : list 가운데 양수를 걸러보자
# filter() 함수 : filter(함수, 매개변수)

def positive(x): 
    return x > 0
print(list(filter(positive, [1,2,3,-1,-2,-3] ))) 


print(list(filter(lambda x : x > 0 ,[1,2,3,-1,-2,-3] )))