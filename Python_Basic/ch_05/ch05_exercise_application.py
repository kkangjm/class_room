
import ch05_exercise_module as my

data = [13, 12, 10, 11, 6, 8, 9, 7, 10, 12, 14, 16, 14, 15, 17, 20, 23, 22, 24, 27]

def mov_evar(data, day):

    for i in range(len(data)):
        if i >= (day-1):
            avr_data = data[i-(day-1):i+1]
            avr_5 = my.average(avr_data)
            print (i, ":", avr_data, avr_5)


mov_evar(data, 10)