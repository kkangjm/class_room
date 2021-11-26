import random

def PC_num():
    selected = []
    for i in range(3):
        num = random.randint(0, 9)
        while num in selected:
            num = random.randint(0, 9)
        selected.append(num)
    return selected

def USER_num():
    selected = []
    for i in range(3):
        print(i + 1, end='')
        num = int(input('번째 번호(0~9) = '))
        while num in selected :
            num = int(input('다른 값을 입력해주세요. = '))
        selected.append(num)

    return selected

# 게임 플레이
def play_ball():
    pc = PC_num()
    print(pc)
    strike = 0
    ball = 0
    while True:
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
    play_ball()