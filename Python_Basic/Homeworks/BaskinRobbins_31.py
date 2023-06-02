import random
import time

def bskn_31(last_num = 31):

    print('>>Lets play!!\n')

    play_cnt = 0
    user_turn = random.choice([True, False])

    while True :
        if user_turn is True:
            print('\n>> USER turn')
            for i in range(3) :
                play_cnt += 1

                if play_cnt == last_num :
                    print('>> ', play_cnt)
                    print('>> PC Win !!')
                    return

                if i == 2 :
                    print('>> ', play_cnt)
                    user_turn = False
                    break

                else :
                    act = input('>>  {} (0:stay, 1:hit) : '.format(play_cnt))
                    if int(act) == 0 :
                        user_turn = False
                        break


        else :
            print('\n>> PC turn')
            for j in range(3) :
                play_cnt += 1

                if play_cnt == last_num:
                    print('>> ', play_cnt)
                    print('>> USER Win !!')
                    return

                elif play_cnt >= (last_num - 3):
                    print('>> ', play_cnt)
                    time.sleep(1)
                    if play_cnt == (last_num - 1):
                        user_turn = True
                        break

                else :
                    print('>> ', play_cnt)
                    time.sleep(1)
                    pc_act = random.choice(['stay', 'hit'])
                    if pc_act == 'stay':
                        user_turn = True
                        break
                    elif j == 2 :
                        user_turn = True
                        break


# function Test
if __name__ == "__main__":
    bskn_31()

