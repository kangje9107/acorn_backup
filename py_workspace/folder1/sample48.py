f = open("c:/temp/data.txt",'r', encoding='utf8')

# for i in range(1, 11): 
#     data = i
#     #f.write(data)
#     pass


# #file 전체를 읽어서 str로 반환
# file = f.read() #file을 처음 읽을때는 seek(0)가 생략되어있는 것임
# print("1:",file)

# #EOF에 있으므로 read() 두번은 안됨
# file = f.read()
# print(file)


#.seek() method : 
    # * 0 -- start of stream (the default); offset should be zero or positive
    # * 1 -- current stream position; offset may be negative
    # * 2 -- end of stream; offset is usually negative
#


# line= f.readline()
# print(line)

# line = f.readline()
# print(line)

# line = f.readline()
# print(line)

# line = f.readline()
# print(line)

# line = f.readline()
# print(line)  #EOF 

# print(type(line))
# print(len(line))

#readline(): 더이상 읽을 줄이 없을 경우 None 반환
# while True: 
#     line =f.readline()
#     if not line: #EOF
#         break
#         pass
#     print(line,end='')
    
#     pass

# >>> line = "jihye\n"
# >>> help(line.replace)
# Help on built-in function replace:

# replace(old, new, count=-1, /) method of builtins.str instance
#     Return a copy with all occurrences of substring old replaced by new.

#       count
#         Maximum number of occurrences to replace.
#         -1 (the default value) means replace all occurrences.

#     If the optional argument count is given, only the first count occurrences are
#     replaced.


f.seek(0)
lines = f.readlines()
print(type(lines))
print(lines) #한 행을 \n까지 포함해서 읽음 

for line in lines: 
    print(line.replace('\n',''))
    pass


f.close()

#input() 함수는 아무것도 안치면 empty string 이 들어온다. 
# while True: 
#     inputData = input("입력하세요:")
#     print(type(inputData))
#     if not inputData: #empty str = False 
#         break 
#         pass



