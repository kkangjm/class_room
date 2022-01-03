
import random

def PC_num():
    selected = []
    for i in range(3):
        num = random.randint(0, 9)
        while num in selected: num = random.randint(0, 9)
        selected.append(num)
    return selected

def USER_num():
    selected = []
    for i in range(3):
        while True :
            print(i+1, end='')
            try :
                num = int(input('번째 번호(0~9) = '))

            except ValueError :
                print('숫자를 입력해주세요.')

            else :
                while num in selected :
                    num = int(input('다른 값을 입력해주세요. = '))

                if 0 <= num and num <= 9 :
                    selected.append(num)
                    break
                else : print('(0~9)사이로 주세요.')

    return selected

# 게임 플레이
def play_ball(try_num=10):
    pc = PC_num()
    # print(pc)
    strike = 0
    ball = 0
    for i in range(try_num):
        print('\n>>', i,'번째 시도')
        user = USER_num()
        print(user)

        for j in range(3):
            if user[j] == pc[j] : strike += 1
            elif user[j] in pc : ball += 1

        print('{} Strike, {} Ball'.format(strike,ball))
        if strike == 3 : break
        strike = 0
        ball = 0


# function test
if __name__ == '__main__':

    play_ball(20)