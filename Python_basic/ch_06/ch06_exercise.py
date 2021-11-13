
import statistics

data_x = [1.48, 1.83, 2.17, 2.84, 3.61, 3.28, 2.83, 2.34, 1.93, 1.61]
data_y = [2.64, 4.83, 7.07, 11.01, 15.15, 13.45, 10.75, 7.78, 5.39, 3.41]

def cor_factor(x, y):

    avr_x = statistics.mean(x)
    avr_y = statistics.mean(y)
    sum = 0
    for i in range(len(x)):
        sum = sum + (x[i]-avr_x)*(y[i]-avr_y)
        print(i, sum)
    covar = sum / len(x)
    cor_fac = covar / (statistics.pstdev(x)*statistics.pstdev(y))
    return cor_fac

print(cor_factor(data_x, data_y))


