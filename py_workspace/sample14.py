#tuple
#()는 생략 가능하므로 단일요소로는 tuple을 정의할 수 없음
t1 = (1) # int 
t2 = (1,) # tuple
t3 = 1, # tuple
print(type(t1))
print(type(t2))
print(type(t3))

t = (0,1,2,3,4,5)
result = t[-3:-1]

t4 = (1,2,3)
t5 = 4, 5
result = (t4 + t5) * 200



