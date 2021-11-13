import datetime 		# datetime 모듈 불러오기

# datetime 타입 데이터 생성
dateTime = datetime.datetime(2019, 1, 1)
print(dateTime)

# date shift test
date = datetime.date(2019, 1, 1)
print('reference date =', date)

date_1 = date - datetime.timedelta(days=1)
print('shifted date =', date_1)

# datetime 연산
print('date gap =', date-date_1)

# datetime 항목 분리
time_now = datetime.datetime.now()
print('time_now =', time_now)
print('date =', time_now.date())
print('year =', time_now.year)
print('month =', time_now.month)
print('day =', time_now.day)
print('weekday =', time_now.weekday())
print('time =', time_now.time())

# string to datetime 변환
date_str = '2021-04-07 14:33'
print(type(date_str))
date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')
print(type(date_obj))
print(date_obj)

