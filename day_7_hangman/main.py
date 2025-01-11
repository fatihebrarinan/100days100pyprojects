import random
import hangman_ASCII
import hangman_kelimeler
from replit import clear

print(hangman_ASCII.logo)

kelime = random.choice(hangman_kelimeler.word_list)
liste = []
kelime_uzunluğu = len(kelime)
kalan_can = 6

for i in range(kelime_uzunluğu):
    liste += "_"
print(liste)
end_of_game = False
while not end_of_game:
    tahmin = input("\nBir harf veya kelime tahmin et:  ").lower()
    clear()
    doğru_tahmin = False

    if tahmin == kelime:

        end_of_game = True
        doğru_tahmin = True
        for n in range(kelime_uzunluğu):
            liste = [tahmin[n] if tahmin[n] != '_' else liste[n] for n in range(kelime_uzunluğu)]

    else:

        for i in range(kelime_uzunluğu):
            if kelime[i] == tahmin:
                liste[i] = tahmin
                doğru_tahmin = True

    print(liste)

    if not doğru_tahmin:
        print(f"\nTahminin {tahmin}. Yanlış.")
        kalan_can -= 1
        print(hangman_ASCII.stages[kalan_can])

    if "_" not in liste:
        print("Tebrikler! kazandınız!")
        end_of_game = True

    if kalan_can == 0:
        print(f"Kaybettiniz! Oyun Bitti. Kelime {kelime} idi.")
        end_of_game = True