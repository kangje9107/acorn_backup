import pandas as pd

import os

def my_func(x):
    x = str(x)[:8]
    return x
    pass

for i in ['2016','2017','2018']:

    dust1 = pd.read_csv(f'C:/app/weather/{i}/{i}년 1분기.csv', encoding='cp949')
    dust2 = pd.read_csv(f'C:/app/weather/{i}/{i}년 2분기.csv', encoding='cp949')
    dust3 = pd.read_csv(f'C:/app/weather/{i}/{i}년 3분기.csv', encoding='cp949')
    dust4 = pd.read_csv(f'C:/app/weather/{i}/{i}년 4분기.csv', encoding='cp949')

    dust = pd.concat([dust1,dust2,dust3,dust4], ignore_index=True)

    dust['지역'] = dust['지역'].agg(lambda x:x[:2])
    dust['측정일시'] = dust['측정일시'].agg(my_func)

    dust_1 = dust[['SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25','측정일시','지역']]

    dust_group = dust_1.groupby(['지역','측정일시'])[['SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].mean()
    
    dust_group.to_csv(f'C:/app/weather/{i}/{i}년.csv', encoding='cp949')
    
    pass

dust_1.info()
dust_1
dust_group

dust_group.head()
dust1 = pd.read_csv('C:/app/weather/2018/2018년 1분기.csv', encoding='cp949')
dust2 = pd.read_csv('C:/app/weather/2018/2018년 2분기.csv', encoding='cp949')
dust3 = pd.read_csv('C:/app/weather/2018/2018년 3분기.csv', encoding='cp949')
dust4 = pd.read_csv('C:/app/weather/2018/2018년 4분기.csv', encoding='cp949')

dust = pd.concat([dust1,dust2,dust3,dust4], ignore_index=True, sort=True)

dust.info()

dust.loc[1914085]