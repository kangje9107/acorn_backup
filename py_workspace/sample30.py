# Switch statment

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

switch = { 
    1: func1,
    2: func2,
    3: func3,
    4: func4, 
    5: func5
} # Dict 


while 1:
    number = int(input(prompt))
    if(number == 99):
        print("Quitting...")
        break
        pass
    #print("\t- switch[%d]"%(number), switch[number])
    switch[number]() #Dict에 저장된 함수 호출 코드

    pass
