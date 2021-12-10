
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 샘플 데이터
df_raw = pd.read_csv('ch06_data.csv', delimiter=';')
df_data = pd.DataFrame(np.array(df_raw['n_passengers'], dtype=np.float), index=df_raw['month'], columns=['passengers'])
# print(df_data)

# 데이터 전처리
df_data['scaled'] = np.log1p(df_data['passengers'])         # 로그 스케일 변환
df_data['scaled_diff'] = df_data['scaled'].diff(periods=1)  # 1차 차분
df_data = df_data.dropna(axis=0)                            # 차분 결과 없는 1행 삭제
print(df_data)

# 데이터 플로팅
fig, ax = plt.subplots(3, 1, num='Data Plot', figsize=(6,8))
df_data.plot(y='passengers', ax=ax[0], title='Raw Data')
df_data.plot(y='scaled', ax=ax[1], title='Scaled Data')
df_data.plot(y='scaled_diff', ax=ax[2], title='Scaled Diff Data')
plt.tight_layout()

plt.show()

