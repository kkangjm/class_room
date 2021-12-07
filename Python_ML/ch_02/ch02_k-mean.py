from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# 샘플 데이터 생성
x, y = make_blobs(n_samples=100, centers=4, n_features=2, cluster_std=2, random_state=7)
points = pd.DataFrame(x, y).reset_index(drop=True)
points.columns = ['x', 'y']
# print(points.head())

# k-means clustering 실행
kmeans = KMeans(n_clusters=4)   # 클러스터 4개
kmeans.fit(points)

# k-means 결과
result = points.copy()
result['cluster'] = kmeans.labels_
print(result)

# 데이터 플로팅
points.plot(kind='scatter', x='x', y='y', c=kmeans.labels_, cmap='Paired')
plt.show()