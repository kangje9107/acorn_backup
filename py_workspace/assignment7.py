#12/5 
#Factorial Expression 
#Recursive Call

prompt="Factorial Expression: "


#Recursive call (재귀호출)
def recur_factorial(number):
    if (number == 1 ) | (number == 0) : 
        print(number,"=", end=" ")
        return 1
        pass
    # elif (number < 0 ): 
    #     print("잘못입력하셨습니다. ")
    #     return '' 
    #     pass
    
    else : 
        #print(number,"x", end=" ")
        return number * recur_factorial(number-1)
    pass

inputNumber = int(input(prompt))
print(recur_factorial(inputNumber))


# def factorial(inputNumber): 
#     result = 1
#     print(str(inputNumber) + "! = ", end="")
#     for i in range(inputNumber,0,-1):
#         if i == 1 : 
#             print(i)
#             pass
#         else:
#             print(str(i)+"*",end="")
#             result = result * i
#             pass
#     return result
#     pass 


# inputNumber = int(input(prompt))
# print(factorial(inputNumber))
