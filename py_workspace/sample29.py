# C의 Switch statment -> python function으로....

prompt ='''
----------------------
        menu
----------------------
1. Menu1 -> func1
2. Menu2 -> func2
3. Menu3 -> func3
4. Menu4 -> func4
5. Menu5 -> func5
99. Quit

Select a number: '''

def func1(): 
    print("-func1() invoked")
    pass
def func2(): 
    print("-func2() invoked")
    pass
def func3(): 
    print("-func3() invoked")
    pass
def func4(): 
    print("-func4() invoked")
    pass
def func5(): 
    print("-func5() invoked")
    pass


while 1: #Infinit loop 생성
    number = int(input(prompt))
    if(number==99): #탈출조건
        print("Quiting...")
        break
    elif(number==1):
        #print("Menu1")
        func1()
    elif(number==2):
        #print("Menu2")
        func2()
    elif(number==3):
        #print("Menu3")
        func3()
    elif(number==4):
        #print("Menu4")
        func4()
    elif(number==5):
        #print("Menu5")
        func5()
    else:
        print("Wrong Number")
    pass