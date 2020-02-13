A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}
print(type(A))
C = A & B 
C = A.intersection(B)

C = A | B 
C = A.union(B)

C = A - B
C = A.difference(B)

#SET.add(VALUE) : 값 1개만 추가
A.add(7)
#.remove(VALUE) : 특정 값 삭제
A.remove(2)
print(A)

#SET.apdate(VALUE) : 여러 값 추가, 단 DICT는 KEY만 들어감.
A.update() #OK
A.update((1000,2000),[12312,0],{3000,4000}, {10000:'v1', 20000:'v2'})


A.update([1,100,99])
A.remove(100)

A.update((1000,2000),[12312,0],{3000,4000})

