
# tkinter 모듈 호출
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# event loop 창 숨기기
Tk().withdraw()

# file open dialog 호출
filename = askopenfilename(
                           initialdir="C:/Users/user/Desktop/",  # 초기 경로
                           title="Select Mode file",             # 파일 열기창 title
                           filetypes=(("CSV files", "*.csv"), ("all files", "*.*")) # 파일 타입 필터
                           )

# 파일명 출력
print(filename)

