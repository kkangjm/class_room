from matplotlib import pyplot as plt
import numpy as np

# 데이터1 : 심플 데이터
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, -1, 2, 3, 1, 1, 2]

# 데이터2 : 사인파
start = 0
end = 2 * np.pi
dx = 1000
t = np.linspace(start, end, dx)
sin_t = np.sin(t)

# 그래프 사이즈
plt.figure(figsize=(6,8))

# 그래프 #1
ax1 = plt.subplot(3,1,1)
plt.plot(x, y, label='simple', color='blue', linestyle='solid', marker='o')
plt.xlabel('Time')
plt.ylabel('Value')
plt.axis((0, 7, -2, 4))      #축의 범위 : (xmin, xmax, ymin, ymax)
plt.legend()    # 범례 표시

# 그래프 #2
ax2 = plt.subplot(3,1,2, sharex=ax1, sharey=ax1)    # ax1과 x, y축 공유
plt.bar(x, y, label='simple', color='blue', width=0.25)
plt.grid(True)  # 그리드 표시
plt.legend()    # 범례 표시

# 그래프 #3
plt.subplot(3,1,3)
plt.plot(t, sin_t, label='sine', color='red', linestyle='dashed')
plt.ylim([-2, 2])     # Y축의 범위: [ymin, ymax]
plt.grid(True)  # 그리드 표시
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.legend()    # 범례 표시

# 그래프 그리기
plt.tight_layout()
plt.show()
