#sample58.py
#To test exception handling using try 



try: 
    #4/0  # =? ZerodivisionError 발생가능하겠구나 유추 가능 
    
    import os
    print('-cwd: ', os.getcwd())
    f = open('C:/app/py_workspace/sample99.py','r') #error 발생하자마자 try문을 나감 
    pass #end try 

except(FileNotFoundError, ZeroDivisionError, IndexError) as e:
    print('- Multi-except block invoked')
    print(e)

    if isinstance(e,FileNotFoundError): #내장함수 : 첫번째가 두번째의 instance면 T
        print('isinstance: True')
        
        f = None ##Our Idea
        pass
    else: 
        print('isinstance: False')
    pass

finally: #except block보다 먼저 수행됨
    print('- finally block invoked.')
    f.close()
    print('- f.close() OK')
    #except ZeroDivisionError as e: #Error를 담는 변수는 짧게 만드는게 관습  
    # print(type(e))
    # print(id(e))
    # print(dir(e))
    # print(e)
    # print(e.__str__())
    pass #end pass  