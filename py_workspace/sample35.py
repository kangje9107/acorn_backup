def add(number1, number2):
    return (number1 + number2)
    pass

lambda num1,num2: (num1+num2)


def div(num1, num2):
    return(num1/num2)
    pass

divFunc = lambda num1, num2 : (num1/num2)
divResult = divFunc(2,3)
print(divResult)


def nextYear(thisyear): 
    return (thisyear + 1)
    pass

nextyearFunc = lambda thisyear : (thisyear + 1)
result = nextyearFunc(2019)
print(result)


def sayHello(name):
    return "Hello, %s" % name
    pass

hello = lambda name : "Hello %s" % name
result = hello('jH')
print(result)

def sayHelloEveryone(): 
    return " Hello, Everyone "
    pass
hello2 = lambda :"Hello Everyone"
result = hello2()
print(hello2)
print(result)


#lambda expression의 target function : lambda식으로 변환할 함수

def sayHello2(name = "ys", age="24"): 
    return "hello , %s, %d" %(name, age)
    pass
hello3 = \
    lambda \
        name='noone',\
        age =24: \
        "hello, %s, %d" %(name, age)
result1 = hello3()
result2 = hello3('trinity')
result3 = hello3('trinity', 25)
print(result1)

