
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# 샘플 데이터
df_raw = pd.read_csv('ch06_data.csv', delimiter=';')
df_data = pd.DataFrame(np.array(df_raw['n_passengers'], dtype=np.float), index=df_raw['month'], columns=['passengers'])
# print(df_data)

# 데이터 전처리
df_data['scaled'] = np.log1p(df_data['passengers'])         # 로그 스케일 변환
df_data['scaled_diff'] = df_data['scaled'].diff(periods=1)  # 1차 차분
df_data['scaled_diff2'] = df_data['scaled'].diff(periods=2) # 2차 차분
df_data = df_data.dropna(axis=0)                            # 차분 결과 없는 1행 삭제
print(df_data)


# Raw 데이터 ACF 분석
fig1, ax1 = plt.subplots(2, 1, num='Raw Data', figsize=(6,8))
df_data.plot(y='scaled', ax=ax1[0], title='Raw Data')
plot_acf(df_data['scaled'], title='Raw data ACF', lags=25, ax=ax1[1])
plt.tight_layout()

# 1차 차분 데이터 ACF 분석
fig2, ax2 = plt.subplots(2, 1, num='1st Differencing', figsize=(6,8))
df_data.plot(y='scaled_diff', ax=ax2[0], title='1st Differencing Data')
plot_acf(df_data['scaled_diff'], title='Diff data ACF', lags=25, ax=ax2[1])
plt.tight_layout()

# 2차 차분 데이터 ACF 분석
fig3, ax3 = plt.subplots(2, 1, num='2nd Differencing', figsize=(6,8))
df_data.plot(y='scaled_diff2', ax=ax3[0], title='2nd Differencing Data')
plot_acf(df_data['scaled_diff2'], title='Diff2 data ACF', lags=25, ax=ax3[1])
plt.tight_layout()

plt.show()

