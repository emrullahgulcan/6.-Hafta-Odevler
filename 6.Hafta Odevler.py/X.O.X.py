import random
tahta = [["___","___","___"],
         ["___","___","___"],
         ["___","___","___"]]
x_durumu = []
o_durumu = []
kazanma_olcutleri = [
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[1,2]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]],
]
kazanma_olcutleri.sort()
X = "pc"
O = "kullanici"
sira = 0
while True:
    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 2)
    sira+=1
    if sira%2 == 0:
        print("oyun sirasi pc de")
        isaret = "X".center(3)
        x = str(random.randint(0, 2)).ljust(30)
        y = str(random.randint(0, 2)).ljust(30)
        print("oyun sirasi =", isaret)
    else:
        print("oyun sirasi kullanicida")
        isaret = "O".center(3)
        x = input("soldan saga dogru (1,2,3):")
        y = input("yukaridan asagiya dogru (1,2,3):")
        print("oyun sirasi =",isaret)

    try:
        x = int(x)
    except ValueError:
        print("yanlis deger girdiniz,siranizi kaybettiniz")
        continue
    if x<1 or x>3:
        print("yanlis deger girdiniz,siranizi kaybettiniz")
        continue

    try:
        y = int(y)
    except ValueError:
        print("yanlis degergirdiniz, siranizi kaybettiniz")
        continue
    if x < 1 or x > 3:
        print("yanlis deger girdiniz,siranizi kaybettiniz")
        continue


    x-=1
    y-=1
    tahta[y][x] = isaret
    if sira % 2 == 0:
        x_durumu+=[[y,x]]
    else:
        o_durumu+=[[y,x]]
    x_durumu.sort()
    o_durumu.sort()
    for i in kazanma_olcutleri:
        if x_durumu == i:
            print("oyunu kazandiniz,tebrikler 'X'",)
            quit()
        elif o_durumu == i:
            print("oyunu kazandiniz,tebrikler 'O'")
            quit()