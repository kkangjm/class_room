import numpy as np
import pandas as pd
import datetime

# dataframe 생성 : date index
date = pd.date_range("20210101", periods=6)
col_name = ['A','B','C','D']
np.random.seed(1)
df = pd.DataFrame(np.random.randn(6, 4), index=date, columns=col_name)
print(df)

# 데이터 수정
df.loc['20210101', 'D'] = 1
df.loc['20210101'][2] = 2
df.iloc[1]['B'] = 3
df.iloc[2][0] = 4
print(df)

# 행 데이터 추가
new_date = datetime.datetime(2021, 1, 7)
df.loc[new_date] = [1,2, None, 4]
print(df)

# 열 데이터 추가
df['SUM'] = df['A'] + df['B'] + df['C']
print(df)

# index로 행, 열 삭제
drop_date = datetime.datetime(2021, 1, 4)
df = df.drop([drop_date], axis=0)
df = df.drop(columns=['D'], axis=1)
print(df)

# 순서로 행, 열 삭제
df = df.drop([df.index[1],df.index[4]], axis=0)
df = df.drop(df.columns[1], axis=1)
print(df)



