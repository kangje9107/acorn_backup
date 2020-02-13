#open('경로','열기모드값')
#파일구분자를 | 말고 /로 쓰면 운영체제 공통이라 에러가 안남 

f = open('C:/temp/fileopen112.txt','w') #운영체제 공통 path separator
# f = open('./fileopen111.txt','w') # Relative Path

# f = open('C:\temp\fileopen111.txt','w') #불가 
# f = open('C:\\temp\\fileopen111.txt','w') #윈도 가능,비추

for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
    pass

f.close()

print(type(f))
print(id(f))
print(f)

#오픈만 하고 닫지않으면 메모리 누수가 발생 
#f.close() #자원반납코드 (Resource Releasing Code )




