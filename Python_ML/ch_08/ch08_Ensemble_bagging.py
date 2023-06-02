import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
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

# Bagging 모델 구축 : DecisionTree, 부트스트랩 샘플링 0.05, OOB 평가
bag_model = BaggingClassifier(
    DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=42),
    n_estimators=500,
    max_samples=0.05,
    bootstrap=True,
    n_jobs=-1,
    oob_score=True
)

# 모델 학습
bag_model.fit(train_input,train_target)

# 모델 훈련 결과 평가
y_predict = bag_model.predict(test_input)
print('>>훈련 스코어 =', round(accuracy_score(test_target,y_predict), 2))
print('>>OOB 스코어 = ', round(bag_model.oob_score_, 2))

# 분류 테스트 : 꽃받침 길이(6cm), 꽃받침 폭(4cm), 꽃잎 길이(2cm), 꽃잎 폭(1cm)
new_data = [[6, 4, 2, 1]]
print('\n>>분류 테스트 =',new_data[0])
print('>>분류 예측 결과 =', flowers[bag_model.predict(new_data)[0]])
