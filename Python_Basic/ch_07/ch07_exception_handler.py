
a = [0,1,2]

try :
    n = int(input ('index = '))
    print (a[n])
    b = a[1] / a[0]

except IndexError :
    # print ("인덱스가 잘못 되었습니다.")
    print(a[2])

except ZeroDivisionError as err :
    print (err)

finally :
    print ("finish")

