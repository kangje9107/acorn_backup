import pandas as pd
import os


df_gapminder = pd.read_csv('doit_pandas\data\gapminder.tsv', sep = '\t')
          # <class 'pandas.core.frame.DataFrame'>

if df_gapminder is not None:
    print('1. df.shape : ', df_gapminder.shape)  # df.shape : data 목록의 크기 확인, 차원정보
    print('2. df.columns:', type(df_gapminder.columns)) df.columns : data 변수의 열 정보 확인
    print('3. df.dtypes: ', df_gapminder.dtypes ) # df.dtypes : 각 변수의타입이 뭐냐
    print(df_gapminder.columns) 
    print(df_gapminder.info()) #df.info : 데이터 정보 종합 세트 **** 이걸 사용하면 됨
    
    #1. list이므로 iteration 가능 
    for column in df_gapminder.columns : 
        print('\t-column:',column)
        pass 
    pass
    
    #.2 list 로 형변환 가능
    l_columns = list(df_gapminder.columns)
    
pass


