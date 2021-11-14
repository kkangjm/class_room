import numpy as np
import pandas as pd

# dataframe 생성 : date index
date = pd.date_range("20210101", periods=30)
col_name = ['A','B','C','D']
np.random.seed(1)
df = pd.DataFrame(np.random.randn(30, 4), index=date, columns=col_name)

# dataframe 출력
print(df)                                   # 기본 출력
print('Dataframe head >>\n', df.head(5))    # 상위 5행
print('Dataframe tail >>\n', df.tail(5))    # 하위 5행
pd.set_option('display.max_row', None)      # 모든 행 출력
pd.set_option('display.max_columns', None)  # 모든 열 출력
print(df)

# 데이터 반복 처리 : iloc
for i in range(3):
    print(i, 'row =', df.index[i], df.iloc[i,0])

# 행 데이터 반복 처리 : iterrows
for index, row in df.iterrows():
    print(index, row['A'])

# 행 데이터 반복 처리 : iterrows
for index, row in df.iteritems():
    print(index, row[1])

# 전체 데이터 반복 처리 : itertuples
for row in df.itertuples():
    print(row.Index, row[1])

# 데이터 반복 처리 : 특정 열의 데이터
for data in df['A']:
    print(data)

# 데이터 프레임 Excel로 출력하기
df.to_excel('dataframe.xlsx', sheet_name='Sheet1')

# Excel 데이터 가져오기
xlsx_file = pd.ExcelFile('dataframe.xlsx')
df_xlsx = pd.read_excel(xlsx_file, 'Sheet1', index_col = 0)
print(df_xlsx)

