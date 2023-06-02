
# CSV 모듈 호출
import csv

# csv_sample.csv 파일 열기
f = open('csv_sample.csv', 'r', encoding='utf-8')

# 데이터 불러오는 객체 생성
csv_rd = csv.reader(f)

# 반복문을 이용하여 한줄씩 불러오기
for line_data in csv_rd:
    print (line_data)

# csv_sample.csv 파일 닫기
f.close()
