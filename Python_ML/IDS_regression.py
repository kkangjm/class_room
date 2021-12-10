
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# event loop 창 숨기기
Tk().withdraw()

# file open dialog 호출
filename = askopenfilename(
                           initialdir="C:/Users/user/Desktop/",  # 초기 경로
                           title="Select Mode file",             # 파일 열기창 title
                           filetypes=(("xlsx files", "*.xlsx"),) # 파일 타입 필터
                           )

# 데이터 읽기
xlsx_file = pd.ExcelFile(filename)
# xlsx_file = pd.ExcelFile('sample_data2.xlsx')
df_xlsx = pd.read_excel(xlsx_file, sheet_name=0)
print(df_xlsx)

start_row_num = 0
for i in range(10):
    if str(df_xlsx.iloc[i][0]).isnumeric()==True :
        start_row_num = i
        break

# 데이터 열 이름 읽기
x_label = df_xlsx.columns[0]
y_label = df_xlsx.columns[1]

# 사이킷런에 훈련을 위해 2차원 배열 형태로 변환
input_data = np.array(df_xlsx[x_label][start_row_num:]).reshape(-1, 1)
target_data = np.array(df_xlsx[y_label][start_row_num:]).reshape(-1, 1)
# print(input_data)
# print(target_data)

# 테스트 세트 : 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(input_data, target_data, test_size=0.2, random_state=1)

# 다항 데이터 생성 : include_bias 는 x^0차 데이터로 무조건 1 -> 의미 없음
polynomial_order = 3
poly_features = PolynomialFeatures(degree=polynomial_order, include_bias=False)
train_poly = poly_features.fit_transform(train_input)
test_poly = poly_features.fit_transform(test_input)
print('>>다항식 계수 =', poly_features.get_feature_names())

# 다항 회귀 모델 훈련
lr = LinearRegression()
lr.fit(train_poly, train_target)
print('>>           =', lr.coef_)
print('>>Y절편 =', lr.intercept_)

# 알고리즘 평가
print('>>훈련 스코어 =', lr.score(train_poly, train_target))
print('>>테스트 스코어 =', lr.score(test_poly, test_target))

# 임의의 데이터 예측
new_data = [[5]]
new_data = poly_features.fit_transform(new_data)
predict = lr.predict(new_data)
print('>>예측 결과 : {0} -> {1:4.2f}'.format(new_data[0,0], float(predict[0])))

# 예측 모델
X_new = np.linspace(0, 10, 100).reshape(100, 1)
X_new_poly = poly_features.transform(X_new)
y_new = lr.predict(X_new_poly)

# 데이터 플로팅
plt.scatter(train_input, train_target, label='train set', color='blue') # 훈련 세트 산점도
plt.scatter(test_input, test_target, label='test set', color='green')   # 테스트 세트 산점도
plt.scatter(new_data[0, 0], predict[0], marker='^', color='red', s=60)  # 임의 데이터
plt.plot(X_new, y_new, linewidth=2, label="Predictions", color='black') # 예측 모델
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
plt.show()
