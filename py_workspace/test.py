##1
# data = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } #set

# for i in data: 
#     print(i)
#     pass

## 2

# for i in range(2,10, 2): 
#     for j in range(1, 10): 
        
#         print('{}x{}={}'.format(i,j,i*j))
        
#         pass
#     pass

## 3
A = 1
B = 2
(A, B) = (B, A)
print(A, B)

##4
 #func1, func2, func3


# def func1():
#     print('func1')
#     pass
# def func2():
#     print('func2')
#     pass
    
# def func3():
#     print('func3')
#     pass

# switch={
#     1:func1,
#     2:func2, 
#     3:func3
# }

# inputNum = int(input("put a number :"))
# switch[inputNum]()

##5
# class Calculator:
#     def __init__(self):
#         super().__init__()
#         pass

#     def add(self, a, b):
#         return a + b
#         pass
#     def sub(self, a, b):
#         return a-b
#         pass
#     def mul(self, a, b):
#         return a*b
#         pass
#     def div(self, a, b):
#         return a/b
#         pass
#     pass


##6
# I = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# result = list(filter(lambda num:True if (num%2!=0)else False,I))
# print(result)