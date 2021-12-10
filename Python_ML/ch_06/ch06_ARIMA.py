
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

# Warning 메세지 숨기기 (옵션)
import warnings
warnings.filterwarnings(action='ignore')

# 샘플 데이터
df_raw = pd.read_csv('ch06_data.csv', delimiter=';')
df_data = pd.DataFrame(np.array(df_raw['n_passengers'], dtype=np.float), index=df_raw['month'], columns=['passengers'])
# print(df_data)

# 데이터 전처리
df_data['scaled'] = np.log1p(df_data['passengers'])
df_data['scaled_diff'] = df_data['scaled'].diff(periods=1)
df_data = df_data.dropna(axis=0)
print(df_data)

# ARIMA 모델
model = ARIMA(df_data['scaled'], order=(2,1,2))
model_fit = model.fit(trend='c', full_output=True, disp=1)
print(model_fit.summary())

# 향후 데이터 예측
fore_periods = 5
fore_value, stdErr, fore_bound = model_fit.forecast(steps=fore_periods)
fore_date = pd.date_range(df_data.index[-1], freq='M', periods=fore_periods+1)[1:]
df_forecast = pd.DataFrame(np.expm1(fore_value), index=fore_date, columns=['passengers_forecast'])
print(df_forecast)

# 데이터 플로팅
fig, ax = plt.subplots(num='Data Plot', figsize=(10,6))
model_fit.plot_predict(1, len(df_data)+fore_periods, ax=ax)
plt.show()