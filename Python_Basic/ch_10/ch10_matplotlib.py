
from matplotlib import pyplot as plt

# 데이터
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, -1, 2, 3, 1, 1, 2]

# 그래프 사이즈
plt.figure(figsize=(8,4))

# 타이틀 표시
plt.title('Test Plotting')

# 축 제목
plt.xlabel('Time')
plt.ylabel('Value')

# 축 범위
plt.xlim([0, 6])      # X축의 범위: [xmin, xmax]
plt.ylim([-3, 4])     # Y축의 범위: [ymin, ymax]

# 데이터 설정
plt.plot(x, y, label='simple')

# 그리드 표시
plt.grid(True)

# 범례 표시
plt.legend()

# 그래프 그리기
plt.show()
