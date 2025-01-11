from replit import clear
from art import logo

print(logo)
print("Gizli açık artırma programına hoş geldin!\n")
son = False
defter = {}
while not son:
    isim = input("Adın ne?: ")
    ödeme = input("ne kadar ödüyorsun?: ₺")
    defter[isim] = ödeme
    devam = input("Daha fiyat veren var mı? (evet-hayır): ")
    clear()
    if devam == "hayır":
        son = True
        liste = []
        isimler = []
        for i in defter:
            isimler.append(i)
            liste.append(defter[i])
        a = max(liste)
        b = liste.index(a)
        c = isimler[b]
        print(f"Kazanan {a}₺ ile {c}!")
