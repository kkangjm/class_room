
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


# 데이터 세트 생성
m = 300
x_data = 10 * np.random.rand(m,1)
y_data = (3*x_data) + 5 + 2*np.random.randn(m, 1)

# 테스트 세트 : 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(x_data, y_data, test_size=0.2, random_state=12)


# SGD 모델 훈련을 위한 최적 epoch 찾기
sr = SGDRegressor(tol=1e-3, penalty=None, eta0=0.1, random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(0, 100):
    sr.partial_fit(train_input, train_target.ravel())

    train_score.append(sr.score(train_input, train_target))
    test_score.append(sr.score(test_input, test_target))

plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()


# SGD 선형 회귀 모델 훈련 : MSE 손실함수, epoch 50, verbose=3
sr = SGDRegressor(max_iter=50, tol=1e-3, penalty=None, eta0=0.1, random_state=42)
sr.fit(train_input, train_target.ravel())
print("\n>>훈련 Epoch = 50")
print('>>훈련 스코어 =', sr.score(train_input, train_target))
print('>>테스트 스코어 =', sr.score(test_input, test_target))

# 선형 회귀식 계수
print('>>선형 회귀 모델 : ', end='')
print('y = {0:4.2f}x + {1:4.2f}'.format(sr.coef_[0], sr.intercept_[0]))

# 결과 출력
y_predicted = sr.predict(x_data)
plt.scatter(x_data, y_data, s=10)
plt.plot(x_data, y_predicted, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

