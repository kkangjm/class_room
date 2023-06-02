
# 샘플 데이터 리스트
data = [13, 12, 24, 19, 6, 8, 9, 7, 10, 12]

# data 리스트 사이즈 확인
n = len(data)

# 리스트 사이즈가 2 이상의 경우
if n > 1 :
    sum = 0     # 합계 저장용 변수 초기화

    # 리스트 각 요소의 합계
    # for value in data :
    #     print(value)
    #     sum = sum + value

    for i in range(n):
        print(i, data[i])
        sum = sum + data[i]

    # 리스트 데이터 평균 계산
    average = sum / n
    print('average =', average)

    sum_devi = 0    # 편차 합계 저장용 변수 초기화

    # 리스트 각 요소의 편차 합계
    for value in data:
        sum_devi = sum_devi + (value - average)**2

    var = sum_devi / n      # 분산값
    std_devi = var**0.5     # 표준 편차
    print('standard deviation = ', std_devi)


# 데이터 사이즈가 2미만의 경우
else :
    print('not enough')
