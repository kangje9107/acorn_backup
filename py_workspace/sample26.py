#range(끝INT(불포함)) : 0 ~ 끝 INT-1 까지의 정수 발생됨
#range(시작INT, 끝INT(불포함))
#range(시작INT, 끝INT(불포함), 간격값 )  

a = range(0, 1, )


for dansu in range(2,10): 
    for number in range(1,10):
        if dansu % 2 ==0 : 
            continue
            pass
        
        print(dansu,"x",number,"=",dansu*number)

        pass 
    pass
