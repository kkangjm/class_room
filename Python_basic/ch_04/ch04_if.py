
# money = 2000
money = input ('금액 = ')
money = int(money)
# 주머니 상황
pocket = ['card', 'phone']

if money >= 3000 or 'card' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
