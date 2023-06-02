import matplotlib.pyplot as plt
import numpy as np

# 샘플 데이터
np.random.seed(1)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

# 데이터 확인
for i in range(n):
    print('({0:2.2f}, {1:2.2f}) = {2:3.0f}, {3:2.3f}'.format(x[i],y[i],area[i],colors[i]))

# Scatter plot
plt.scatter(x, y)
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='rainbow')
# plt.colorbar()
plt.show()
