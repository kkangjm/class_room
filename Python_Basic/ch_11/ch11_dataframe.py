
import numpy as np
import pandas as pd

# dataframe 생성 : date index
date = pd.date_range("20210101", periods=6)
col_name = ['A','B','C','D']
np.random.seed(1)
df = pd.DataFrame(np.random.randn(6, 4), index=date, columns=col_name)
print(df)

# index, columns
print('index = ', df.index)
print('column = ',df.columns)

# row 위치로 데이터 불러오기
print(df.iloc[0]['A'])
print(df.iloc[0, 0])
print(df.iloc[0:2, 0:2])

# index 기준으로 데이터 불러오기
print(df.loc['20210104'])
print(df.loc['20210104', 'B'])
print(df.loc[date[3], 'B'])
print(df.loc['20210104':'20210106', ['C', 'D']])
