
import statistics

class DataAnalysis :

    def average(self, data):
        n = len(data)
        sum = 0
        for value in data:
            sum = sum + value

        return sum / n


    def dev(self, data):
        n = len(data)
        avr = self.average(data)
        sum_devi = 0
        for value in data:
            sum_devi = sum_devi + (value - avr) ** 2

        var = sum_devi / n
        return var


    def std_dev(self, data):
        var = self.dev(data)
        return var ** 0.5


    def cor_factor(self, x, y):

        avr_x = statistics.mean(x)
        avr_y = statistics.mean(y)
        sum = 0
        for i in range(len(x)):
            sum = sum + (x[i] - avr_x) * (y[i] - avr_y)
        covar = sum / len(x)
        cor_fac = covar / (statistics.pstdev(x) * statistics.pstdev(y))
        return cor_fac

if __name__ == '__main__':

    calc = DataAnalysis()

    data_x = [1.48, 1.83, 2.17, 2.84, 3.61, 3.28, 2.83, 2.34, 1.93, 1.61]
    data_y = [2.64, 4.83, 7.07, 11.01, 15.15, 13.45, 10.75, 7.78, 5.39, 3.41]

    print('average =', calc.average(data_x))
    print('deviation =', calc.dev(data_x))
    print('std. deviation =', calc.std_dev(data_x))
    print('correlation fac. =', calc.cor_factor(data_x,data_y))