import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


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

# AdaBoost 모델 생성
abc_model = AdaBoostClassifier(
            base_estimator=DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=42),
            n_estimators=5, ## 반복수 또는 base_estimator 개수
            learning_rate=0.5, ## 스텝 사이즈
        )

# 모델 훈련
abc_model.fit(train_input,train_target)

# 모델 훈련 결과 평가
y_pred_rf = abc_model.predict(test_input)
print('>>훈련 스코어 =',round(accuracy_score(y_pred_rf,test_target),2))

# 분류 테스트 : 꽃받침 길이(6cm), 꽃받침 폭(4cm), 꽃잎 길이(2cm), 꽃잎 폭(1cm)
new_data = [[6, 4, 2, 1]]
print('\n>>분류 테스트 =',new_data[0])
print('>>분류 예측 결과 =', flowers[abc_model.predict(new_data)[0]])

# AdaBoosting 훈련 과정
n_estimator = len(abc_model.estimators_)
fig = plt.figure(figsize=(10, 15), facecolor='white')

for i in range(n_estimator):
    ax = fig.add_subplot(2, 3, i+1)
    plot_tree(abc_model.estimators_[i], max_depth=2, filled=True, class_names=flowers, feature_names=feature_names)
    ax.set_title(f'{i+1} tree')

plt.show()

