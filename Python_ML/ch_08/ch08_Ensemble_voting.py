import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# 데이터 불러오기 : 붓꽃 분류 예제
data = datasets.load_iris()
input_data = data['data']       		# 입력 데이터 : 꽃의 특징
target_data = data['target']    		# 타겟 데이터 : 꽃 종류 (0 ~ 2)
feature_names = data['feature_names']   	# 꽃 특징들의 명칭
flowers = data['target_names']          	# 꽃 종류를 이름으로 나타낸 것

iris_df = pd.DataFrame(input_data, columns=feature_names)
iris_df['species'] = target_data

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(input_data, target_data,
                                                                      stratify=target_data,
                                                                      test_size=0.2, random_state=5)

# 약한 학습 모델
log_model = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='auto')
dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=42)
svm_model = SVC(kernel='rbf', C=10, gamma=1,probability = True)

# Voting 모델 : hard
voting_model = VotingClassifier(
    estimators=[('lr',log_model),('dt',dt_model),('svc',svm_model)],
    voting='hard'
)

# 앙상블 모델 학습
voting_model.fit(train_input,train_target)

# 모델 비교
print('>>학습 모델별 훈련 스코어')
for model in (log_model,dt_model,svm_model,voting_model):
    model.fit(train_input,train_target)
    y_predict = model.predict(test_input)
    print(model.__class__.__name__," : ",round(accuracy_score(test_target,y_predict),2))


# 분류 테스트 : 꽃받침 길이(6cm), 꽃받침 폭(4cm), 꽃잎 길이(2cm), 꽃잎 폭(1cm)
new_data = [[6, 4, 2, 1]]
print('\n>>분류 테스트 =',new_data[0])
print('>>분류 예측 결과 =', flowers[voting_model.predict(new_data)[0]])
