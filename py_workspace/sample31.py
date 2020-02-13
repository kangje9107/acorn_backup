def add(num1, num2):
    print('- add(num1:{}, num2:{})'.format(num1, num2))

    return num1 + num2
    pass

#result = add(1, 2)
result = add(num2=2, num1=1)
#print(add(1,2))

def say_myself(name, man=True, old=10):
    print('-say_myself({},{},{})'.format(name,man,old))
    pass

say_myself("ys",24)
