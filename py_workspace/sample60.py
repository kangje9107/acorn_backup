class IdentityError(Exception): 
    #최상위 object class method __str__를 overriding
    def __str__(self): 
        print('- IndentityError::__str__invoked.')
        
        return '**본인인증 실패**'
    pass #end class

def transfer(name): 
    if (name != 'Joseph'):
        raise IdentityError()
        pass
    pass



try: 
    transfer('Koseph')
except (IdentityError) as e:

    print("본인인증 실패.")
    print('-'*50)
    print(e)
    print(dir(e))
    # print(dir(e.__traceback__)) #오류 발생시 line 등의 정보
    # print(e.__str__) #overridng
    pass
finally: 
    pass