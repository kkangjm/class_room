import statistics

def average(data):
    n = len(data)
    sum = 0
    for value in data :
        # sum = sum + value

        try :
            sum = sum + value
        except TypeError:
            sum = sum + float(value)

    return  sum / n


# function test
if __name__ == '__main__':
    # test_data = [1.48, 1.83, 2.84, 3.61]
    test_data = [1.48, 1.83, '2.17', 2.84, 3.61, '3.28', 2.83, 2.34, '1.93', 1.61]
    print('average =', average(test_data))

    n = len(test_data)

    print('before =', test_data)

    for i in range(n):
        print(type(test_data[i]))
        if str(type(test_data[i])) == "<class 'str'>" :
            print ('발견', i)
            test_data[i] = float(test_data[i])

    print('after = ', test_data)




    print('결과=',statistics.mean(test_data))