
# 데이터 저장
f = open('data.txt', 'w')

for i  in range(10):
    data = '%d번째 줄 \n' % i
    print(data)
    f.write(data)

f.close()


# # 데이터 읽기
# f = open('data.txt', 'r')
#
# while True :
#     data = f.readline()
#     if not data : break
#     print(data)
#
# f.close()
