
l =[  1, 23, 8, 11, 56, 77, 18, 29, 33, 44, 44, 77, 100, 98, 55, 20, 7, 2]

#오름차순
def ascending(List):
    for i in range(0, len(List)) :
        for j in range(i+1,len(List) ):
            if List[i]>=List[j] : 
                List[i],List[j] = List[j], List[i]
                pass
            pass
        pass
    return List
    pass

#내림차순
def descending(List):
    for i in range(0, len(List)) :
        for j in range(i+1,len(List) ):
            if List[i]<=List[j] : 
                List[i], List[j] = List[j], List[i]
                pass
            pass
        pass
    return List
    pass

#Mode(최빈값) 
def Mode(List):
    resultMode = dict() #최빈값과 빈도수를 dict로 담음
    maxFreq = 0 #최빈값의빈도수
    valueFreq = 0

    maxFreq = List.count(i) for i in set(List) if (List.count(i) > maxFreq)
    for i in set(List):
        if List.count(i) > maxFreq :
            maxFreq = List.count(i) #최종 가장 큰 빈도를 maxFreq에 담게됨
            
            pass
        pass
    

    for i in list(set(l)):
        if l.count(i) == Count:
            mode.add(i)

    return mode





    if len(resultMode) == 0 : 
        print('최빈값 없음')
    else :
        print("최빈값: ", List)
    pass

#Median(중앙값)
def Median(List):
    resultMedian = 0
    if len(List) % 2 == 0 : 
        resultMedian = (List[(len(List)/2)] + List[(len(List/2)+1)]) / 2 
    else: 
        resultMedian = List[(len(List)/2)] 
        pass
    return resultMedian
    pass


switch = {
    1: lambda List:ascending(List),
    2: lambda List:descending(List)
}

     
#inputList = list()
#inputList = input("List:")



inputNumber= int(input("1:ascending order\n2:descending order : "))
print(switch[inputNumber](l))

print()



#median 

