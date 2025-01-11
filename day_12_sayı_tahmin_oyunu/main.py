from art import logo
import random
import os

son = False


def guess(tahmin):
    global hak
    if tahmin > sayı:
        hak = hak - 1
        print("Sayı tahmininden daha küçük.")
    elif tahmin < sayı:
        hak = hak - 1
        print("Sayı tahmininden daha büyük.")
    else:
        print(f"Tebrikler! Doğru tahmin ettin. Sayı {sayı} !")
        global son
        son = True


print(logo)
print(
    "Sayıyı tahmin et oyununa hoş geldin.\n1 ile 100 arasında bir sayı tuttum."
)


def oyna():
    global son
    global hak
    global sayı
    zorluk = input("Zorluk seç ('kolay' veya 'zor' yaz).\n")
    if zorluk == "kolay":
        hak = 10
    else:
        hak = 5

    sayı = random.randint(1, 100)

    while hak > 0 and son == False:
        print(f"Sayıyı bilmek için {hak} hakkın var.")
        tahmin = int(input("Tahmin et: "))
        guess(tahmin)
    if hak == 0:
        print(f"Sayı {sayı} idi.")
        son = True

    if son == True:
        devam = input("Tekrar oynamak istiyor musun? ('e' / 'h')\n")
        if devam == "e":
            os.system('clear')
            son = False
            oyna()
        if devam == "h":
            print("Oynadığın için teşekkürler.")


oyna()