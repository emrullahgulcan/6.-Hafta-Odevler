kullanici = input("Aklinizda bir sayi tuttu iseniz oyunumuza baslayabiliriz,lutfen entere basiniz")
import random
pctahmin = random.randint(0,100)
print("pc tahmini =",pctahmin)
while True:

    kullanici_inputu = input("sayi kucukse +,buyukse - yazin :" )
    if kullanici_inputu == "-":
        print("kullanici inputu = ",kullanici_inputu)
        pctahmin =random.randint(0,pctahmin)
        print("pc tahmini =",pctahmin)
    elif kullanici_inputu == "+":
        print("kullanici inputu = ",kullanici_inputu)
        pctahmin = random.randint(pctahmin,100)
        print("pc tahmini =", pctahmin)
    else:
        print("kullanici inputu =",input("enter"))


