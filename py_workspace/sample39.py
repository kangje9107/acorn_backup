#f = open("c:/temp/data.txt",'a', encoding='utf8')
#with가 close 해줌 

# with open('data.txt', 'a',encoding='utf8') as f: 
#     f.write("Append-7\n")
#     f.write("Append-8\n")
#     pass

import sys #built-in module 
# print(type(sys))
# print(id(sys))
# print(dir(sys))
# print(sys)



#print(type(sys.argv))
# print(id(sys.argv))
print(sys.argv)
print(len(sys.argv))

for arg in sys.argv: 
    print('- arg:', arg)
    pass

for arg in sys.argv[1:]: 
    print(arg.upper(),end=" ")
    pass

#import 구문 : run안해도 module을 실행시킴 
# import temp
# print('-name:', temp.name )


# def tempFunc():
#     print('-temp::tempFunc() invoked.')
#     pass

