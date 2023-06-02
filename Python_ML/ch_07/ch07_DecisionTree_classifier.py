from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import pandas as pd

# 데이터 불러오기 : 붓꽃 분류 예제
data = datasets.load_iris()
input_data = data['data']       # 입력 데이터 : 꽃의 특징
target_data = data['target']    # 타겟 데이터 : 꽃 종류 (0 ~ 2)

feature_names = data['feature_names']   # 꽃 특징들의 명칭
flowers = data['target_names']          # 꽃 종류를 이름으로 나타낸 것
print('>>꽃 특징 : {}'.format(feature_names))
print('>>꽃 종류 [0, 1, 2] : {}'.format(flowers))

iris_df = pd.DataFrame(input_data, columns=feature_names)
iris_df['species'] = target_data
# print(iris_df.head(5))  # raw data 확인

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(input_data, target_data,
                                                                      stratify=target_data,
                                                                      test_size=0.2,
                                                                      random_state=5)

# DecisionTreeClassifier 알고리즘 훈련
train_depth = 2
dt = DecisionTreeClassifier(criterion='entropy', max_depth=train_depth, random_state=42)
dt.fit(train_input, train_target)

# 예측 결과 출력
print('>>훈련 스코어 =', dt.score(train_input, train_target))
print('>>테스트 스코어 =', dt.score(test_input, test_target))
print('>>인자별 중요도 \n', feature_names, '\n', dt.feature_importances_)

# 분류 테스트 : 꽃받침 길이(6cm), 꽃받침 폭(4cm), 꽃잎 길이(2cm), 꽃잎 폭(1cm)
new_data = [[6, 4, 2, 1]]
print('\n>>분류 테스트 =',new_data[0])
print('>>분류 예측 결과 =', flowers[dt.predict(new_data)[0]])

# DecisionTree 출력
plot_tree(dt, max_depth=train_depth, filled=True, class_names=flowers, feature_names=feature_names)
plt.show()

