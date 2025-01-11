from art import logo
from replit import clear
import math
import time


def çarpma(n1, n2):
    return n1 * n2


def toplama(n1, n2):
    return n1 + n2


def çıkarma(n1, n2):
    return n1 - n2


def bölme(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return print("Payda sıfır olmaz!")


def üslü(n1, n2):
    try:
        result = pow(n1, n2)
        return result
    except OverflowError:
        return print("sayı çok büyük")


def karekök(a):
    return math.sqrt(a)


def sinüs(a):
    return math.sin(math.radians(a))


def cosinüs(a):
    return math.cos(math.radians(a))


def tanjant(a):
    return math.tan(math.radians(a))


def kotanjant(a):
    return 1 / math.tan(math.radians(a))


print("Pyhton hesap makinesi programı.")

işlemler = {
    "*": çarpma,
    "+": toplama,
    "-": çıkarma,
    "/": bölme,
    "**": üslü,
    "karekök": karekök,
    "sin": sinüs,
    "cos": cosinüs,
    "tan": tanjant,
    "cot": kotanjant,
}


def hesap_makinesi():
    print(logo)
    sayı1 = float(input("Bir sayı girin: "))
    print("*\n+\n-\n/\naᵇ (** yaz)\n√ (karekök yaz)\nsin\ncos\ntan\ncot")

    son = False
    while not son:
        işlem = input("\nBir işlem seçin: ")
        if işlem == "*" or işlem == "+" or işlem == "-" or işlem == "/" or işlem == "**":
            if işlem == "**":
                sayı2 = float(input("Üssü girin: "))
            else:
                sayı2 = float(input("Sonraki sayıyı girin: "))

            fonksiyon = işlemler[işlem]
            cevap = fonksiyon(sayı1, sayı2)
            cevap = float(cevap)
            cevap = round(cevap, 4)
            print(f"{sayı1} {işlem} {sayı2} = {cevap}")

            devam = input(f"{cevap} ile işleme devam et? e/h: ")
            if devam == "e":
                sayı1 = cevap
            else:
                son = True
                clear()
                hesap_makinesi()

        elif işlem == "karekök" or işlem == "sin" or işlem == "cos" or işlem == "tan" or işlem == "cot":
            fonksiyon = işlemler[işlem]
            cevap = fonksiyon(sayı1)
            cevap = round(cevap, 4)
            print(f"{işlem} {sayı1} = {cevap}")

            devam = input(f"{cevap} ile işleme devam et? e/h: ")
            if devam == "e":
                sayı1 = cevap
            else:
                son = True
                clear()
                hesap_makinesi()

        else:
            print("Geçersiz giriş.")
            son = True
            print("Program 5 saniye sonra yeniden başlatılacak.")
            time.sleep(5)
            clear()
            hesap_makinesi()


hesap_makinesi()