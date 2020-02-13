# Data 먼징 작업시 유용한 Methods
# 문자열 객체의 Method test : type string 에만 적용 
#문자열 Counting : count() Method
string = "hobby"
print(string.count('b'))

#문자열 Indexing 
#1. find() method : 가장 첫번째 값의 인덱스 반환, 없는 문자 넣으면 '-1' 나옴
a = "python is the best choice."
print(a.find("p")) 
print(a.find("k"))

#2. index() = find()가장 첫번째 값의 인덱스 반환, 없는 문자열 넣으면 오류 반환
#print(string.index("K"))

#문자열 삽입 : join() method
#활용 : 전화번호같은 데이터 수집시 '-' 삽입, CSV 형식으로 기업 데이터 교환시 사용
print('-'.join("12345689"))
print(','.join(['a','b','c','d']))

scores = ['98','100','77','22','100'] #list 
print(','.join(scores))

#문자열.upper() , 문자열.lower() : 대문자/소문자로 변환
#문자열.strip() , 문자열.lstrip(), 문자열.rstip() : 공백 제거, 중간 공백은 제거안함 
#문자열.replace() : 문자열 치환
#문자열.split(delimiter) : seperater =delimiter를 기준으로 문자열 쪼개어 List로 반환, default는 공백문자
targetString = "           as dfzxcv  "
print(targetString.strip().upper())
s = targetString.replace("as","Life").replace("dfzxcv","is too short").strip()
print(s)
print(s.replace(" ",""))
print(s.split())

t = "A: B :C :D "
print(t.replace(" ","").split(":"))






