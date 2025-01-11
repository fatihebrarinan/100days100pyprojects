rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

print("Taş-Kağıt-Makas oyununa hoş geldiniz! ")
devam = 1
while devam == 1:
    seçim = int(input("\nTaş için 0, \nKagıt için 1, \nMakas için 2 yaz.\n"))
    print("Sen:")
    if seçim == 0:
        print(rock)
    elif seçim == 1:
        print(paper)
    elif seçim == 2:
        print(scissors)

    print("Bilgisayar:")
    bilgisayar = random.randint(0, 2)
    if bilgisayar == 0:
        print(rock)
    elif bilgisayar == 1:
        print(paper)
    elif bilgisayar == 2:
        print(scissors)

    if bilgisayar == seçim:
        print("Berabere.")
    if (bilgisayar == 1 and seçim == 0) or (bilgisayar == 2 and seçim == 1) or (bilgisayar == 0 and seçim == 2):
        print("Bilgisayar kazandı.")
    if (bilgisayar == 0 and seçim == 1) or (bilgisayar == 1 and seçim == 2) or (bilgisayar == 2 and seçim == 0):
        print("Sen kazandın.")
        devamlılık = input("Tekrar? (evet/hayır)\n")
        if devamlılık == "evet":
            devam == 1
        elif devamlılık == "hayır":
            devam == 0
            print("Oynadığın için teşekkürler.")
        else:
            print("Geçerli cevap değil.")


