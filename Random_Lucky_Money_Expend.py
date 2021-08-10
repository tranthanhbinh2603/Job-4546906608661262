import random as r

money = int(input("Ban muon chia bao nhieu tien? "))
minimum = int(input("So tien nho nhat ban muon chia: "))
count = int(input("So nguoi chia: "))

for i in range(1, 21):
    temp = r.randint(minimum,money - ((count - i)*minimum))
    money -= temp
    print(temp)
    

