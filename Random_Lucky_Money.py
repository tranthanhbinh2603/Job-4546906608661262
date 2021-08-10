import random as r

money = 500000
minimum = 1000
count = 20

for i in range(1, 21):
    temp = r.randint(minimum,money - ((count - i)*minimum))
    money -= temp
    print(temp)
    

