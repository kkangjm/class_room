import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 데이터 불러오기 : 타이타닉 예제
data = pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')
# print(data.head(5))        # Raw 데이터
# print(data.isna().sum())    # 데이터 확인 : Null 값 여부

# 데이터 전처리
data['Sex'] = data['Sex'].map({'male':0, 'female':1})   # 성별 데이터를 숫자로 변환
target = data['Survived']                               # 타겟 데이터 세트
data.drop(labels=['Name', 'Survived'], axis=1, inplace=True)  # 필요없는 데이터 제거 : 이름, 생존여부
# print(data)

# dataframe 열 이름 변경
data.rename(columns={'Siblings/Spouses Aboard':'Spouses',
                     'Parents/Children Aboard':'Children'}, inplace=True)

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(data, target,
                                                                      stratify=target,
                                                                      test_size=0.2,
                                                                      random_state=5)

# 로지스틱 회귀 알고리즘 훈련 : 훈련 반복 횟수 1000회
lr = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='auto')
lr.fit(train_input, train_target)

# 회귀 함수
np.set_printoptions(precision=3,suppress=True)  # numpy print 자릿수
print('>>변수 =', data.columns.values)
print('>>결정계수 =', lr.coef_[0])

# 예측 결과 출력
print('\n>>테스트 세트 데이터\n', test_input.iloc[0:5])
print('\n>>테스트 세트 z값\n', lr.decision_function(test_input[0:5]))
print('\n>>테스트 세트 예측 확률\n', lr.predict_proba(test_input[0:5]))
print('\n>>테스트 세트 예측 결과\n', lr.predict(test_input[0:5]))

# 생존 테스트 : 2등석, 남자, 25세, 혼자, 혼자, 50달러
new_data = [2, 0, 25, 0, 0, 50]
new_pred = lr.predict([new_data])
print('\n>>생존 테스트 =',new_data)
print('>>[사망 확률, 생존 확률] =', format(lr.predict_proba([new_data])))
if(new_pred[0]==0): print('>>사망 ㅜㅜ\n')
else: print('>>생존 ^^\n')
