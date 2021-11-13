
# CSV 모듈 호출
import csv

# csv_sample.csv 파일 생성
f = open('csv_sample.csv', 'w', encoding='utf-8', newline='')

# 데이스 쓰는 객체 생성
csv_wr = csv.writer(f)

# 리스트 데이터 쓰기
csv_wr.writerow([1, 'LFD', 'MR16DD'])
csv_wr.writerow([2, 'LFD', 'MR18DD'])
csv_wr.writerow([3, 'LFD', 'MR20DD'])
csv_wr.writerow([4, 'LJL', 'HR13DD'])
csv_wr.writerow([5, 'LJL', 'HR16DE'])

# csv_sample.csv 파일 닫기
f.close()

