from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt

# 입력 데이터
length = np.array(
    [0.08, 0.61, 0.79, 0.90, 0.95, 0.98, 1.68, 1.68, 1.86, 1.92,
     2.09, 2.19, 2.20, 2.32, 2.40, 2.68, 2.68, 2.74, 2.81, 3.05,
     3.25, 3.44, 4.22, 4.31, 4.56, 4.58, 4.85, 5.90, 6.13, 6.15,
     6.34, 6.36, 6.61, 6.67, 6.70, 6.97, 7.26, 7.27, 7.87, 7.89,
     8.32, 8.37, 8.63, 9.13, 9.37, 9.39, 9.51, 9.54, 9.57, 9.91])

weight = np.array(
    [20.39, 16.89, 18.26, 19.57, 15.50, 22.01, 23.04, 23.10, 27.15, 16.44,
     26.06, 24.95, 25.23, 23.36, 26.45, 16.56, 24.64, 21.10, 25.39, 23.38,
     26.15, 20.69, 19.31, 29.12, 30.69, 26.26, 21.89, 43.00, 38.74, 38.39,
     47.83, 37.71, 45.34, 54.65, 52.98, 44.35, 63.06, 54.63, 66.41, 69.48,
     72.30, 80.25, 75.71, 87.50, 95.20, 97.68, 99.70, 101.13, 102.65, 104.81])

# 테스트 세트 : 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(length, weight, test_size=0.2, random_state=12)

# 사이킷런에 훈련을 위해 2차원 배열 형태로 변환
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

# 2차항 데이터 추가
train_2nd = np.column_stack((train_input ** 2, train_input))
test_2nd = np.column_stack((test_input ** 2, test_input))

# 선형 회귀 모델 훈련
lr = LinearRegression()
lr.fit(train_2nd, train_target)

# 선형 회귀식 계수
print('>>다항 회귀 모델 : ', end='')
print('y = {0:4.2f}x^2 + {1:4.2f}x + {2:4.2f}'.format(lr.coef_[0], lr.coef_[1], lr.intercept_))

# 알고리즘 평가
print('>>훈련 스코어 =', format(lr.score(train_2nd, train_target), '2.2f'))
print('>>테스트 스코어 =', format(lr.score(test_2nd, test_target), '2.2f'))

# 훈련 결과 평가
test_prediction = lr.predict(test_2nd)                         # 테스트 세트 예측값
err_mean = mean_absolute_error(test_target, test_prediction)    # 테스트 세트 MSE
print('>>테스트 평균 오차 =', format(err_mean, '4.2f'))

# 임의의 데이터 예측
new_data = [7]
predict = lr.predict([[new_data[0]**2, new_data[0]]])
print('>>예측 결과 : {0} -> {1:4.2f}'.format(new_data[0], predict[0]))

# 데이터 플로팅
plt.scatter(train_input, train_target, label='train set', color='blue') # 훈련 세트 산점도
plt.scatter(test_input, test_target, label='test set', color='green')   # 테스트 세트 산점도
point = np.arange(0, 11)
plt.plot(point, lr.coef_[0]*point**2 + lr.coef_[1]*point + lr.intercept_, label="Predictions", color='black')   # 예측 모델
plt.scatter(new_data[0], predict[0], marker='^', color='red', s=60)     # 임의 데이터
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.legend()
plt.show()

