import time		# time 모듈 불러오기

time.time()	            # UTC 1970년 1월 1일 0초 이후 누적초
print(time.localtime(time.time()))	# 시간대 기준으로 단위 구분
time.ctime()		# 현재 날짜 및 시간

print(time.time())

# 시간 딜레이
print(time.ctime())
time.sleep(1)
print(time.ctime())

# 현재 시간 포멧 변경
print(time.strftime('%X', time.localtime(time.time())))

while True :
    print(time.strftime('%X', time.localtime(time.time())))
    time.sleep(1)


