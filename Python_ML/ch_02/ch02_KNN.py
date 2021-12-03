import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# 데이터 #1 : 토마토
tomato_size = [38.1, 39.4, 39.8, 43.5, 44.5, 44.5, 44.8, 45.0, 45.0, 46.1, 46.5, 46.5, 47.3, 48.0, 48.0, 48.0, 49.5, 49.5, 50.2, 50.3, 51.0, 51.0, 51.7, 52.5, 52.5, 52.5, 52.5, 54.0, 54.0, 55.5, 57.7, 57.8, 59.3, 61.5, 61.5]
tomato_weight = [205.7, 246.5, 289.0, 308.55, 365.5, 382.5, 425.0, 331.5, 382.5, 425.0, 403.75, 425.0, 425.0, 289.0, 510.0, 510.0, 595.0, 595.0, 518.5, 552.5, 488.75, 582.25, 527.0, 578.0, 595.0, 616.25, 612.0, 606.9, 722.5, 850.0, 782.0, 811.75, 786.25, 828.75, 807.5]

# 데이터 #2 : 방울 토마토
miniTomato_size = [14.7, 15.5, 15.9, 16.5, 16.8, 16.9, 17.7, 17.8, 18.0, 18.3, 18.6, 19.5, 21.45, 22.5, 23]
miniTomato_weight = [21.4, 24.0, 22.4, 30.7, 31.4, 27.8, 32.0, 31.7, 31.4, 39.0, 42.9,39.0, 63.0, 63.7, 64]

# 훈련 타겟 데이터 : 토마토 = 1, 방울토마토 = 0
target = [1]*35 + [0]*15

# 훈련 입력 데이터
length = tomato_size + miniTomato_size
weight = tomato_weight + miniTomato_weight
input_data = np.column_stack((length, weight))

# KNN (k-nearest neighbors) 알고리즘 훈련
kn = KNeighborsClassifier(n_neighbors=5) # 근접 이웃 판별 샘플 수 = 5
kn.fit(input_data, target)

# 임의 데이터
new_size = 35   # 28로 테스트 해보기
new_weight = 200
new_data = [new_size, new_weight]

# 임의 데이터 분류 예측
predict = kn.predict([new_data])
distances, indexes = kn.kneighbors([new_data])      # 근접 데이터
print('>>예측 결과 (0 : 방울토마토, 1 : 토마토) = ', predict[0])

# 데이터 플로팅
plt.scatter(input_data[:35, 0], input_data[:35, 1], label='tomato', color='red')
plt.scatter(input_data[36:, 0], input_data[36:, 1], label='mini tomato', color='blue')
plt.scatter(new_data[0], new_data[1], label='new data', marker='^')
plt.scatter(input_data[indexes, 0], input_data[indexes, 1], label='neighbors', marker='D')
plt.xlabel('size')
plt.ylabel('weight')
plt.legend()
plt.show()
