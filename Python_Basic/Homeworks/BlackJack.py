import random
import time


def get_card(num_deck=4):
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    cardset = card * num_deck
    random.shuffle(cardset)
    return cardset


def card2num(card, A=11):
    if card == 'J':
        value = 10
    elif card == 'Q':
        value = 10
    elif card == 'K':
        value = 10
    elif card == 'A':
        value = A
    else:
        value = int(card)
    return value


def blkjc(balance=100):
    print('\n>> Lets play!!')

    remained_bet = 0

    while True:

        card = get_card(4)
        #         print(card)  # Show Card

        card_cnt = 0

        while True:
            if remained_bet == 0:
                try:
                    bet = int(input('\n>> bet (balance = {}$) :  '.format(balance)))
                except ValueError:
                    print("\n>> Wrong number. Betting 0")
                    bet = 0

            else:
                print('\n>> Carry over {}$'.format(remained_bet))
                try:
                    bet = int(input('>> Additional bet (balance = {}$) :  '.format(balance)))
                except ValueError:
                    print("\n>> Wrong number. Betting 0")
                    bet = 0

            if (balance - bet) >= 0:
                break
            else:
                print('>> You bet too much')

        # initialize
        player_card = []
        dealer_card = []
        player_sum = 0
        dealer_sum = 0

        print('\n>> Player Turn')

        # player turn
        while True:

            # open card
            card_now = card[card_cnt]
            player_card.append(card_now)

            if card_now == 'A':
                if input('  A is (0 = 1, 1 = 11) ? ') == '0':
                    card_value = card2num(card_now, 1)
                else:
                    card_value = card2num(card_now, 11)
            else:
                card_value = card2num(card_now)

            player_sum = player_sum + card_value
            card_cnt += 1

            if player_sum > 21:
                print('>> {} = {}, Bust!! : '.format(player_card, player_sum))
                break

            elif player_sum == 21:
                print('>> {} = {}, Black Jack!! : '.format(player_card, player_sum))
                break

            else:
                act = input('>> {} = {}, (0:stay, 1:hit) : '.format(player_card, player_sum))
                if int(act) == 0:
                    print('>> Player score = ', player_sum)
                    break

        print('\n>> Dealer Turn')

        # dealer turn
        while True:

            # open card
            card_now = card[card_cnt]
            dealer_card.append(card_now)

            if card_now == 'A':
                if dealer_sum > 11:
                    card_value = card2num(card_now, 1)
                else:
                    card_value = card2num(card_now, 11)
            else:
                card_value = card2num(card_now)

            dealer_sum = dealer_sum + card_value
            card_cnt += 1

            time.sleep(random.randint(1, 3))

            if dealer_sum >= 17:
                if dealer_sum > 21:
                    print('>> {} = {}, Bust!! : '.format(dealer_card, dealer_sum))
                elif dealer_sum == 21:
                    print('>> {} = {}, Black Jack!! : '.format(dealer_card, dealer_sum))
                else:
                    print('>> {} = {}, Stay!! : '.format(dealer_card, dealer_sum))
                print('>> Dealer score = ', dealer_sum)
                break

            else:
                print('>> {} = {}'.format(dealer_card, dealer_sum))

        # compare score
        if (player_sum > 21) and (dealer_sum > 21):
            remained_bet = remained_bet + (bet * 2)
            balance = balance - bet
            print('>> Draw !! Carry over {}$ (balance = {}$)'.format(remained_bet, balance))

        elif player_sum > 21:
            prize = bet
            balance = balance - prize
            print('>> Player Defeat !!, Lose {}$ (balance = {}$)'.format(prize, balance))
            remained_bet = 0

        elif dealer_sum > 21:
            prize = bet + remained_bet
            balance = balance + prize
            print('>> Player Win !!, Get {}$ (balance = {}$)'.format(prize, balance))
            remained_bet = 0

        elif player_sum > dealer_sum:
            prize = bet + remained_bet
            balance = balance + prize
            print('>> Player Win !!, Get {}$ (balance = {}$)'.format(prize, balance))
            remained_bet = 0

        elif player_sum < dealer_sum:
            prize = bet
            balance = balance - prize
            print('>> Player Defeat !!, Lose {}$ (balance = {}$)'.format(prize, balance))
            remained_bet = 0

        elif player_sum == dealer_sum:
            remained_bet = remained_bet + (bet * 2)
            balance = balance - bet
            print('>> Draw !! Carry over {}$ (balance = {}$)'.format(remained_bet, balance))

        if (balance == 0) and (remained_bet == 0):
            print('\n>> You are bankrupt!!')
            break

        go_sel = input('\n>> STOP?(Y/N) = ')
        if go_sel == 'Y' or go_sel == 'y':
            print('\n>> Your balance = {}$'.format(balance))
            break

    print('\n>> Game Finish!!')


# function Test
if __name__ == "__main__":
    blkjc()
