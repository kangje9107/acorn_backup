#a=[11,2,7,88,99,100]
a = ["1","10","7"]
#a.append(4)
a.sort() #elements 순서대로 정렬
a.reverse() #elements를 현재상태의 거꾸로 뒤집어줌
result = a.index("1")


#요소 삽입 : .append() 추천 
a.insert(0,999) #List의 index가 밀려서 주의해야됨.
a.append(4)
a.remove(88) #List method. 삭제한 요소 뒤의 요소들 인덱스가 당겨짐. index가 아니라 Value를 넣는 것임에 주의
result = a.pop() #List의 맨마지막요소를 끄집어내서 삭제함

a.count("1")


