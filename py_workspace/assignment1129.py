'''
   주어진 일련의 숫자를 정렬하시오.
   (내림차순/오름차순 모두 가능하게)

  1, 23, 8, 11, 56, 77, 18, 29, 33,
   44, 44, 77, 100, 98, 55, 20, 7, 2

    정렬후, 아래의 특성값을 추출하시오.
   (1) 평균 (2) 중위수 (3) 최빈값 

'''

l =[  1, 23, 8, 11, 56, 77, 18, 29, 33, 44, 44, 77, 100, 98, 55, 20, 7, 2]

for i in range(0, len(l)) :
    for j in range(i+1,len(l) ):
        if l[i]>=l[j] : 
            l[i], l[j] = l[j], l[i]
    pass
pass

print(l) 

#최빈값 
a, freq = dict(), 1


for i in range(0, len(l)): 
    for j in range(i+1, len(l)): 
        if l[i] == l[j] : 
            freq += 1
            a[l[i]] = freq
    freq = 1    
            

if len(a) == 0 : 
    print('최빈값 없음')
else :
    print(a.keys()) 
