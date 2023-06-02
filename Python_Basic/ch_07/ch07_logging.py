
import logging

# 로그 생성
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log handler 생성
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력하도록 handler 연결
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 코드 내 로거 활용
for i in range(10):
    logger.info(f'{i}번째 loop입니다.')
