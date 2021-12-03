import random
import time


# 함수 정의

# 선공 결정 : 랜덤 함수

# 반복 (

# if 유저 선공

# 현재 카운터 확인

# GO / STOP 입력

# GO 2번 이상 못 함

# STOP 하면 턴 넘기기  )












def bskn_31(last_num = 31):

    print('>>Lets play!!\n')

    play_cnt = 0
    # 선공 판단
    user_turn = random.choice([True, False])

    while True :
        # 유저 턴
        if user_turn is True:
            print('\n>> USER turn')
            # 번호 호출 기회 max 3회
            for i in range(3) :
                play_cnt += 1
                # 현재 카운터가 31이면 종료
                if play_cnt == last_num :
                    print('>> ', play_cnt)
                    print('>> PC Win !!')
                    return # 함수 리턴 = 종료

                # 이미 두번 번호 불렀으면 턴 넘기기
                if i == 2 :
                    print('>> ', play_cnt)
                    user_turn = False   # 턴 넘기기
                    break   # for문 탈출

                # 위의 두 조건이 아니면 GO / STOP 결정
                else :
                    act = input('>>  {} (0:stay, 1:hit) : '.format(play_cnt))
                    if int(act) == 0 :  # stay 결정시
                        user_turn = False   # 턴 넘기기
                        break   # for 탈출

        # PC 턴
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
                    # 30에서 상대로 넘기고 필승
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
