def fun1(): 
    return "func1"
pass
#간단한 함수를 lambda로 ... 
switch = {
    1: (lambda : "func1"),
    2: (lambda : "func2")
}

choice = 1

switchResult = switch[choice]



