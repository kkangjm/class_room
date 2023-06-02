from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from scipy.special import softmax
import pandas as pd
import numpy as np

# 데이터 불러오기 : 붓꽃 분류 예제
data = datasets.load_iris()
input_data = data['data']       # 입력 데이터 : 꽃의 특징
target_data = data['target']    # 타겟 데이터 : 꽃 종류 (0 ~ 2)

feature_names = data['feature_names']   # 꽃 특징들의 명칭
flowers = data['target_names']          # 꽃 종류를 이름으로 나타낸 것
print('꽃 특징 : {}'.format(feature_names))
print('꽃 종류 [0, 1, 2] : {}'.format(flowers))

iris_df = pd.DataFrame(input_data, columns=feature_names)
iris_df['species'] = target_data
print(iris_df.head(5))  # raw data 확인

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(input_data, target_data,
                                                                      stratify=target_data,
                                                                      test_size=0.2,
                                                                      random_state=5)

# 데이터 전처리 : 정규화
scaler = StandardScaler()   # (xi - mean) / std.dev
scaler.fit(train_input)
train_scaled = scaler.transform(train_input)
test_scaled = scaler.transform(test_input)
print('\n>>train_input\n', train_input[:5])
print('\n>>train_scaled\n', train_scaled[:5])


# 로지스틱 회귀 알고리즘 훈련 : 훈련 반복 횟수 1000회
lr = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='auto')
lr.fit(train_scaled, train_target)

# 회귀 함수
np.set_printoptions(precision=3,suppress=True)  # numpy print 자릿수
print('\n>>결정계수 =\n', lr.coef_)
print('\n>>절편 =', lr.intercept_)

# 예측 결과 출력
print('\n>>테스트 세트 데이터\n', test_scaled[0:5])
decision = lr.decision_function(test_scaled[:5])
print('\n>>테스트 세트 z값\n', decision)
proba = softmax(decision, axis=1)
print('\n>>테스트 세트 예측 확률\n', proba)
print('\n>>테스트 세트 예측 결과 =', lr.predict(test_scaled[:5]))

# 분류 테스트 : 꽃받침 길이(6cm), 꽃받침 폭(4cm), 꽃잎 길이(2cm), 꽃잎 폭(1cm)
new_data = [[6, 4, 2, 1]]
new_scaled = scaler.transform(new_data)
print('\n>>분류 테스트 =',new_data[0])
print('>>분류 예측 결과 =', flowers[lr.predict(new_scaled)[0]])


