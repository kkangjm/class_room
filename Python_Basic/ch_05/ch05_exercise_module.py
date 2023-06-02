
def average(data):
    '''
    평균 계산 함수
    :param data: (int list) 입력 데이터
    :return: (float) 평균값
    '''
    n = len(data) # 리스트 개수 확인
    sum = 0
    for value in data :
        sum = sum + value

    return  sum / n


def std_dev(data):
    '''
    데이터 표준편차 계산
    :param data: 숫자형 리스트
    :return: (Float) 데이터 표준편차
    '''

    n = len(data)
    avr = average(data)
    sum_devi = 0
    for value in data:
        sum_devi = sum_devi + (value - avr)**2

    var = sum_devi / n
    return var**0.5

# function test
if __name__ == '__main__':
    test_data = [13, 12, 24, 19, 6, 8, 9, 7, 10, 12]
    print('average =', average(test_data))
    print('standard deviation = ', std_dev(test_data))