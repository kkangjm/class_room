
def fac(num):
    result = 1
    for i in range(1,num+1) :
        # print (i)
        result = result * i
    return result

if __name__ == '__main__':
    n = int(input('number = '))
    print(fac(n))