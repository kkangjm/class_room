
from matplotlib import pyplot as plt
import numpy as np

# Bar 데이터
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, -1, 2, 3, 1, 1, 2]

# Line 데이터
start = 0
end = 2 * np.pi
dx = 1000
t = np.linspace(start, end, dx)
sin_t = np.sin(t)

# Bar형 그래프
fig, ax1 = plt.subplots()
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Bar Y-Axis')
ax1.axis((0, 6, -2, 4))      # 축의 범위 : (xmin, xmax, ymin, ymax)
bar = ax1.bar(x, y, label='Bar Data', color='blue', width=0.25)

# Line형 그래프
ax2 = ax1.twinx()   # X축 공유
ax2.set_ylabel('Line Y-Axis')
ax2.axis((0, 6, -2, 2))      # 축의 범위 : (xmin, xmax, ymin, ymax)
line = ax2.plot(t, sin_t, label='Line Data', color='red', linestyle=(0,(5,5)))

# 그리드 표시
plt.grid(True)

# 그래그 그리기
plt.tight_layout()  # 그래프 레이아웃 채우기
plt.show()