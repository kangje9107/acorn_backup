#sample57.py : game package에 있는 모듈임. 

#from game.graphic.render import render_test

#from ..graphic.render import render_test
#import 로 실행되면, 모듈을 script file로 수행시킴
print("__name__:",__name__) # 수행당시 실행되고 있는 python script file 명. imported module인 경우에는 module명이 뜸 
print("__package__:",__package__) #scriptfile일 경우에는 None이 뜸, imported module인경우에는 경로가 뜨

import os
print('- os.getcwd():', os.getcwd()) #현재 실행되는 경로 뜸 
#C:\app\py_workspace가나옴.ArithmeticError

from ..sound import echo #sound package의 echo.py file을 쓰겠다. 

print(echo)



#print(render_test)
#render_test()
 