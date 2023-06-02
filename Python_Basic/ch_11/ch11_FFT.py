
import numpy as np
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt

# 샘플링
start = 0   # 시작(s)
end = 1     # 종료(s)
dx = 1000   # 샘플링 속도(hz)

# 대상 시그널
time = np.linspace(start, end, dx)          # 1000hz 샘플링
s1 = 2 * np.sin(10 * 2 * np.pi * time)      # 진폭 : 2.0, 주파수 : 10Hz
s2 = 1 * np.sin(20 * 2 * np.pi * time)      # 진폭 : 1.0, 주파수 : 20Hz
s3 = 0.5 * np.sin(30 * 2 * np.pi * time)    # 진폭 : 0.5, 주파수 : 30Hz
s4 = 1.5 * np.sin(40 * 2 * np.pi * time)    # 진폭 : 1.5, 주파수 : 40Hz
s = s1 + s2 + s3 + s4   # 신호 중첩

print(s)

# FFT
fft_val = fft(s)                            # FFT
fft_norm = fft_val / len(time)              # FFT 결과 정규화
strength = 2 * abs(fft_norm)                # 진폭 2배 (음의 영역 제거)
frequency = fftfreq(dx, (end-start)/dx)     # 주파수 축 설정

# Plot signal
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)              # plot 영역 2x1 중의 1 
plt.plot(time, s)

# plot FFT
plt.subplot(2,1,2)              # plot 영역 2x1 중의 2
plt.xlim(0, 50, 10)             # 양의 주파수 영역만 표시
plt.ylim(0, 3, 0.5)             # 진폭 축 설정
plt.grid()
plt.bar(frequency, strength, color='red', width=0.5)

# show plot
plt.show()
