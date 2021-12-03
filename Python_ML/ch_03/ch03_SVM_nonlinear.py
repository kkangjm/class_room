import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn import svm
import matplotlib.pyplot as plt

# 샘플 데이터 생성
data, target = make_moons( n_samples = 100, noise = 0.15, random_state=42)

# 훈련 데이터 중에서 랜덤으로 테스트 세트 추출
train_input, test_input, train_target, test_target = train_test_split(data, target,
                                                                      stratify=target,
                                                                      test_size = 0.2,
                                                                      random_state=1)

# SVM 알고리즘 훈련
clf = svm.SVC(kernel='rbf', C=10, gamma=1)
clf.fit(train_input, train_target)

# 훈련 결과 평가
clf_predictions = clf.predict(test_input)
print("훈련 스코어 =", clf.score(test_input, test_target))

# 임의 데이터 분류 예측
new_data = [1,0]
print('>>예측 결과(0 : normal, 1 : failure) =', clf.predict([new_data]))


# 데이터 플로팅
plt.scatter(data[:,0], data[:,1], c=target, cmap='RdYlBu')  # 샘플 데이터
plt.scatter(new_data[0], new_data[1], marker='^', color='Green')    # 예측 데이터

# 초평면(Hyper-Plane) 플로팅
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)
ax.contour(XX, YY, Z, colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--', '-', '--'])

# 지지벡터(Support Vector) 플로팅
ax.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=45, facecolors='r')

plt.show()