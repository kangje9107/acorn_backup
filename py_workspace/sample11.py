#List indexing & slicing 

l = [1,2,3,[4,5,6]]
element1=l[0]
element2=l[-2]
result = element1 + element2
inner_list=l[-1][-2]

list1 =[
    1,2,3,
    [
        4,5,6,
        [
            7,8,9
        ]    
    ]
]

IwantThisElemnet = list1[3][-1][2]

a = [1,2,3,['a','b','c'],4,5]
b = a[1:4][-1]

print(b)
