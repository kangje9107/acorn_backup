#두 양수만 덧셈을 수행
def add(num1, num2):

    print('- add({},{}) invoked.' .format(num1,num2))

    if(num1 <= 0) or (num2 <= 0):
        return -1
        pass

    result = num1 + num2
    return result #함수가 즉시 종료됨 
    pass

print(type(add))
print(id(add))
print(add)


func = add()

def add2(addFunction, num1, num2):
    return addFunction(num1, num2)
    pass

result3 = add2(func, 4, 4)

