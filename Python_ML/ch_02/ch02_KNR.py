
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# 입력 데이터
length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )

# 결과 데이터
weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

# 데이터 Z-score 전처리 : (x - mean) / std
length_mean = np.mean(length, axis=0)
length_std = np.std(length, axis=0)
length_scaled = (length - length_mean) / length_std

weight_mean = np.mean(weight, axis=0)
weight_std = np.std(weight, axis=0)
weight_scaled = (weight - weight_mean) / weight_std

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(length_scaled, weight_scaled,
                                                                      test_size=0.25, random_state=5)


# 사이킷런에 훈련을 위해 2차원 배열 형태로 변환
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

# KNN (k-nearest neighbors) 알고리즘 훈련
knr = KNeighborsRegressor()
knr.n_neighbors = 5  # 이웃의 갯수를 5로 설정 : 기본값
knr.fit(train_input, train_target)

# 알고리즘 평가
print('>>k value = ', knr.n_neighbors)
print('>>훈련 스코어 =', format(knr.score(train_input, train_target), '2.2f'))
print('>>테스트 스코어 =', format(knr.score(test_input, test_target), '2.2f'))

# 훈련 결과 평가
test_prediction = knr.predict(test_input)   # 테스트 세트에 대한 예측
err_mean = mean_absolute_error(test_target, test_prediction)  # 테스트 세트에 대한 평균 절댓값 오차
print('>>테스트 평균 오차 =', format(err_mean, '2.2f'))


# 임의의 데이터 예측
new_length = 35
new_data = ([new_length] - length_mean) / length_std
predict = knr.predict([new_data])
distances, indexes = knr.kneighbors([new_data])      # 근접 데이터
print('>>예측 결과 : {0} -> {1}'.format(new_length, predict[0] * weight_std + weight_mean))


# 데이터 플로팅
plt.scatter(train_input, train_target, label='train set', color='blue') # 훈련 세트 산점도
plt.scatter(test_input, test_target, label='test set', color='green') # 테스트 세트 산점도
plt.scatter(new_data[0], predict[0], label='new data', marker='^', color='red', s=60)  # 임의 데이터
plt.scatter(train_input[indexes], train_target[indexes], label='neighbors', marker='D', color='orange')  # k-근접 데이터 산점도
plt.xlabel('Scaled length')
plt.ylabel('Scaled weight')
plt.legend()
plt.show()