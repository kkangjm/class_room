
# CSV 모듈 호출
import csv

# csv_sample.csv 파일 생성
f = open('csv_sample.csv', 'w', encoding='utf-8', newline='')

# 데이스 쓰는 객체 생성
csv_wr = csv.writer(f)

# 리스트 데이터 쓰기
csv_wr.writerow([1, 'Oh_my_girl', 'HYOJUNG'])
csv_wr.writerow([2, 'Oh_my_girl', 'ARIN'])
csv_wr.writerow([3, 'Oh_my_girl', 'YOOA'])
csv_wr.writerow([4, 'aespa', 'KARINA'])
csv_wr.writerow([5, 'aespa', 'WINTER'])

# csv_sample.csv 파일 닫기
f.close()

