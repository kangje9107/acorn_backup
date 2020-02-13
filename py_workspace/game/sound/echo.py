#echo.py

MODULE_NAME = 'echo'

def echo_test():
    print('-echo::echo_test invoked.')
    pass
#본 echo module을 import해돋 lambda는안나옴 Caching때문에
lambdaFunc = lambda : print('-echo::lambdaFunc invoked.') #lamdba 사용을 비추하는예이긴 함

