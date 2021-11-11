
money = 1000
price = 200
ticket = 0

while money > price :
   money = money - price
   ticket += 1

print('buy first =', ticket)


while True :
   money = money - price
   ticket += 1
   if money < price : break

print('buy second =', ticket)
