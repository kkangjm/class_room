
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# 데이터 세트 생성
m = 100
x_data = 10 * np.random.rand(m,1)
y_data = (0.2*(x_data**3)) + (-2*(x_data**2)) + (3*x_data) + 5 + 2*np.random.randn(m,1)

# 테스트 세트 : 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(x_data, y_data, test_size=0.2, random_state=1)

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
new_data = [[3]]
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
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.legend()
plt.show()
