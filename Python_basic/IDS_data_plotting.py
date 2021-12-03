import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from scipy.fftpack import fft, fftfreq
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# event loop 창 숨기기
Tk().withdraw()

# file open dialog 호출
filename = askopenfilename(
                           initialdir="C:/Users/user/Desktop/",  # 초기 경로
                           title="Select Mode file",             # 파일 열기창 title
                           filetypes=(("CSV files", "*.csv"),) # 파일 타입 필터
                           )

# 데이터 읽기
df_data = pd.read_csv(filename)

# dataframe 전처리 : Time 열을 index로 변환
new_index = []  # 새로운 인덱스 생성을 위한 빈 리스트
for index in df_data['Time']:   # dataframe 에서 'Time' 행 하나씩 읽기
    split_time = index.split('d ')[1]   # Time data에서 'd ' 기준 분리하여 뒷 내용
    conv_time = datetime.strptime(split_time, '%H:%M:%S.%f') # 문자열을 시간형으로
    new_index.append(conv_time) # 시간형으로 변환된 데이터를 new_index 리스트에 추가

df_data.index = new_index   # new_index 리스트를 dataframe의 인덱스로 설정
df_data = df_data.drop(columns=['Time'], axis=1)    # 'Time' 열은 삭제

# print(df_data)
# df_data.plot()
# # plt.show()


# FFT 분석 설정
dt_str = df_data.index[1] - df_data.index[0]
dt = float(str(dt_str).split(':00:0')[1])
Fs = (1.0 / dt)     # 샘플링

start = df_data.index[0]  # 시작 시간(s)
end = df_data.index[-1]  # 종료 시간(s)
# print(start)
# print(end)
dx = 1/dt   # 샘플링 주파수(hz)
t_delta = float(str(end-start).split(':00:')[1])   # 데이터 시간차를 실수형으로 변호나

# STFT 설정
N_FFT = 1000         # 윈도우 크기
N_Overlap = 10      # Frame 오버랩 크기


# FFT 분석
fft_val = fft(df_data['Amplitude'])             # FFT 변환
fft_norm = fft_val / len(df_data['Amplitude'])  # FFT 결과 정규화
strength = 2 * abs(fft_norm)                    # 진폭 2배 (음의 영역 제거)
frequency = fftfreq(len(strength), (t_delta)/len(strength))     # 주파수 축 설정

# print(len(strength))
# print(len(frequency)_


plt.figure(figsize=(6,8))

# 데이터 플로팅
plt.subplot(3,1,1)
plt.plot(df_data['Amplitude'])

# FFT 결과 플로팅
plt.subplot(3,1,2)              # plot 영역 2x1 중의 2
plt.xlim(0, 200, 10)             # 양의 주파수 영역만 표시
plt.plot(frequency, strength, color='red')

# STFT 결과 플로팅
plt.subplot(3,1,3)
Spectrum, freqs, t_axis, im = plt.specgram(df_data['Amplitude'],
                                           Fs=Fs, NFFT=N_FFT,
                                           noverlap=N_Overlap,
                                           mode='psd')

plt.tight_layout()  # 그래프 레이아웃 채우기
plt.show()

