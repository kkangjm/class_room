
import matplotlib.pyplot as plt
import numpy as np

# 신호 데이터
dt = 0.001
t = np.arange(0.0, 10.0, dt)
s1 = np.sin(2 * np.pi * 10 * t)
s2 = np.sin(2 * np.pi * 100 * t)
s3 = 0.5 * np.sin(2 * np.pi * 300 * t)

# s2, s3 신호 중첩 시간 설정
s2[t <= 2] = s2[7 <= t] = 0
s3[t <= 6] = s3[9 <= t] = 0

# 노이즈 신호
np.random.seed(1)
nse = 0.01 * np.random.random(size=len(t))

# 신호 중첩
x = s1 + s2 + s3 + nse

# 분석 설정
Fs = int(1.0 / dt)  # 샘플링
N_FFT = 200         # 윈도우 크기
N_Overlap = 10      # Frame 오버랩 크기

# subplot ax1, ax2 생성
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(10,6))

# 신호 그래프
ax1.plot(t, x)
ax1.grid()

# STFT 그래프
Spectrum, freqs, t_axis, im = ax2.specgram(x, Fs=Fs, NFFT=N_FFT, noverlap=N_Overlap, mode='psd')

# 그래프 그리기
plt.show()
