# import sys

# print('- sys.argv:', sys.argv)

# if True : 
#     sys.exit(0) #normal exit
#     print('--------')
#     pass


#----------------------
import pickle as pk
# f = open('obj.dat', 'wb')

# #pk.dump(object, file)
# object = [1,2,3,4,5]
# pk.dump(object, f)
# f.close()

with open('obj.dat','rb') as f:
    #지정된 파일에 저잗왼 파이썬 객체를 현재 실행 메모리로 다시 loading시키는 함수
    l = pk.load(f)
    print(l)
    pass

import os

targetDir = "c://app"
returnValue = os.chdir(targetDir)
print(' - returnValue: ', returnValue)
cwd = os.getcwd()
print('-cwd :', cwd)
# print(os.environ)
# print(type(os.environ))

#PATH환경변수 : 윈도 운영체제에서 실행되는모든 실행명령어를 찾으러 가는 폴더의목록을 저장하고 있는 변수 
#실행명령어가, 이 환경변수에있는 폴더 목록에서 찾지못하면, 보통 '명령어를 찾을수 없습니다"라는 메세지를출력하고 끝냄 
key = 'PATH'
print(os.environ[key])

