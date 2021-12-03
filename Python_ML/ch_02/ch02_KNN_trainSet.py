import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 데이터 #1 : 토마토
tomato_size = [38.1, 39.4, 39.8, 43.5, 44.5, 44.5, 44.8, 45.0, 45.0, 46.1, 46.5, 46.5, 47.3, 48.0, 48.0, 48.0, 49.5, 49.5, 50.2, 50.3, 51.0, 51.0, 51.7, 52.5, 52.5, 52.5, 52.5, 54.0, 54.0, 55.5, 57.7, 57.8, 59.3, 61.5, 61.5]
tomato_weight = [205.7, 246.5, 289.0, 308.55, 365.5, 382.5, 425.0, 331.5, 382.5, 425.0, 403.75, 425.0, 425.0, 289.0, 510.0, 510.0, 595.0, 595.0, 518.5, 552.5, 488.75, 582.25, 527.0, 578.0, 595.0, 616.25, 612.0, 606.9, 722.5, 850.0, 782.0, 811.75, 786.25, 828.75, 807.5]

# 데이터 #2 : 방울 토마토
miniTomato_size = [14.7, 15.5, 15.9, 16.5, 16.8, 16.9, 17.7, 17.8, 18.0, 18.3, 18.6, 19.5, 21.45, 22.5, 23]
miniTomato_weight = [21.4, 24.0, 22.4, 30.7, 31.4, 27.8, 32.0, 31.7, 31.4, 39.0, 42.9,39.0, 63.0, 63.7, 64]

# 훈련 입력 데이터
length = tomato_size + miniTomato_size
weight = tomato_weight + miniTomato_weight
input_data = np.column_stack((length, weight))

# 훈련 타겟 데이터 : 토마토 = 1, 방울토마토 = 0
target = [1]*35 + [0]*15

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(input_data, target,
                                                                      stratify=target,
                                                                      test_size=0.25,
                                                                      random_state=1,
                                                                      shuffle=True)

# 데이터 Z-score 전처리 : (x - mean) / std
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)
train_scaled = (train_input - mean) / std
test_scaled = (test_input - mean) / std

# KNN (k-nearest neighbors) 알고리즘 훈련
kn = KNeighborsClassifier(n_neighbors=5) # 근접 이웃 판별 샘플 수 = 5
kn.fit(train_scaled, train_target)

# 훈련 결과 평가
print('>>테스트 스코어 =', kn.score(test_scaled, test_target))

# 임의 데이터
new_size = 35
new_weight = 200
new_data = ([new_size, new_weight] - mean) / std

# 임의 데이터 분류 예측
predict = kn.predict([new_data])
distances, indexes = kn.kneighbors([new_data])      # 근접 데이터
print('>>예측 결과 (0 : 방울토마토, 1 : 토마토) = ', predict[0])

# 데이터 플로팅
plt.scatter(train_scaled[:,0], train_scaled[:,1], label='train_set', color='orange')
plt.scatter(test_scaled[:,0], test_scaled[:,1], label='test_set', color='yellow')
plt.scatter(new_data[0], new_data[1], label='new_data', marker='^', color='blue')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], label='neighbors', marker='D', color='red')
plt.xlabel('size')
plt.ylabel('weight')
plt.legend()
plt.show()
