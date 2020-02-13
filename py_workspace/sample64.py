# sample64.py

import random as r
#random함수를 이용한, 일정 범위 내의 무작위 정수를 만들어내는 코드. 
#알고리즘때 많이 이용할 코드.
def randomIntRange(start, end):    
    # Formula: 
    #   1) 0 <= X < 1
    #   2) ( 0 x (end - start + 1) ) <= X < ( 1 x (end - start + 1) )
    #   3) int( 0 x (end - start + 1) ) <= X < int( 1 x (end - start + 1) )
    #   4) int( 0 x (end - start + 1) ) + start <= X < int( 1 x (end - start + 1) ) + start
    # 
    #     ex) 5 ~ 13 (start = 5, end = 13)
    #         int( 0 x (13 - 5 + 1)) + 5 <= X < int( 1 x (13 - 5 + 1) ) + 5
    #         int( 0 x 9 ) + 5 <= X < int( 1 x 9 ) + 5
    #         0 + 5 <= X < 9 + 5
    #         5 <= X < 14

    result = int(r.random() * (end - start + 1)) + start

    return result
    pass


for index in range(10000000):
    start = 3
    end = 5

    X = randomIntRange(start, end)
    if (X < start) or (X > end):
        print("{}. X < {} or X > {}: {}".format(index, start, end, X))
        pass
    elif (X == start) or (X == end):
        # print("{}. X == {} or X == {}: {}".format(index, start, end, X))
        pass
    else:
        print('.', end='')
        pass

    pass # end for