import pandas as pd
import random
import time
from termcolor import colored, cprint
text=colored('TOMBALAA', 'blue',)
print("*************")
print(" "+" "+text)
print("*************")

ana_kutle = list(range(10,100))

oyuncu_1 = []
oyuncu_2 = []
i = 1
while i < 11:
    a =random.randint(10,99)
    if not (a in oyuncu_1):
        oyuncu_1.append(a)
        i +=1
k = 1
while k < 11:
    b = random.randint(10,99)
    if not (b in oyuncu_2):
        oyuncu_2.append(b)
        k +=1
#Yukarıda iki oyuncunun 10 sayılık tombala kartları oluşturlmuştur.
print(colored("1.Oyuncunun Kartları : ","red" )+ str(oyuncu_1))
print("****")
print(colored("2.Oyuncunun Kartları : ","red") + str(oyuncu_2))
#Şimdi çekilecek kartların loop'u
while True:
    print(colored("Kart Çekiliyor:..","blue"))
    time.sleep(1)
    take = random.randint(0, len(ana_kutle)-1)
    cekilen_kart = ana_kutle[take]
    ana_kutle.pop(take)
    print(colored("Çekilen Kart : ","red"), str(cekilen_kart))
    time.sleep(1)
    #Çekilen Karı Göndermece Yapıyoruz Burada




    #Bu Arada Çekilen Kartı Uçurma Yapıyoruz
    if cekilen_kart in oyuncu_1 :
        for i in range(0,len(oyuncu_1)):
            if oyuncu_1[i] == cekilen_kart:
                oyuncu_1[i] = ":)"
    if cekilen_kart in oyuncu_2:
        for i in range(0,len(oyuncu_2)):
            if oyuncu_2[i] == cekilen_kart:
                oyuncu_2[i] = ":)"
    #KAZANIM KONTROLÜ ZAMANI
    win_condition = [":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)"]
    if oyuncu_2 == win_condition and oyuncu_1 == win_condition:
        print("Berabere")
        break
    elif oyuncu_2 == win_condition:
        print("Oyuncu 2 Kazandı")
        break
    elif oyuncu_1 == win_condition:
        print("Oyuncu 1 Kazandı")
        break
    print("Anakütle: " + str(ana_kutle))
    print(oyuncu_1)
    print("*****")
    print(oyuncu_2)
    time.sleep(0.5)



