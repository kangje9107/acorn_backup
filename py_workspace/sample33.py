def add_and_mul(a,b):
    return (a+b, a*b)
    pass

result = add_and_mul(1,2)

addResult, mulResult = add_and_mul(1,2)
print(addResult)
print(mulResult)   


a=1
def vartest(b): #a : local var
    global a
    #여기서 사용하는 a는 global변수라고 명시해줘야함 
    a = a + 1

    pass 

vartest(a)
print('-a:',a)