#blackjack projesi
#kurallar özet
#21 i geçen otomatik kaybeder
# eğer puan 17den küçükse yeni kart seçmek zorundasın
#as 1 veya 11 sayılabilir puana göre
import os
import random

if input("Blackjack oynamak istiyor musun? e/h\n") == "e":

  def fonksiyon():

    def sona():
      oyun_devamı = input("Blackjack oynamak istiyor musun? e/h\n")
      if oyun_devamı == "e":
        os.system('clear')
        fonksiyon()
      else:
        print("Oynadığın için teşekkürler.")

    kartlar = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    ben = []
    pc = []
    i = random.randint(0,12)
    k = random.randint(0,12)
    ben.append(kartlar[i])
    ben.append(kartlar[k])
    l = random.randint(0,12)
    pc.append(kartlar[l])
    print(f"Senin kartların {ben}, Skorun: {sum(ben)}\nBilgisayarın ilk kartı {pc}")

    l = random.randint(0,12)
    pc.append(kartlar[l])
    if random.randint(0,1) == 0:
      l = random.randint(0,12)
      pc.append(kartlar[l])

    devam = input("Kart çekmek için 'e' atlamak için 'h' yaz.\n")

    if devam == "e":

      l = random.randint(0,12)
      ben.append(kartlar[l])
      if sum(ben) > 21:
        print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
        print("Kaybettin!")
        sona()
      elif sum(pc) > 21:
        print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
        print("Kazandın!")
        sona()
      else:
        if sum(ben) > sum(pc):
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Kazandın!")
          sona()
        elif sum(pc) > sum(ben):
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Kaybettin!")
          sona()
        else:
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Berabere.")
          sona()
    else:
      if sum(pc) > 21:
        print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
        print("Kazandın!")
        sona()
      else:
        if sum(ben) > sum(pc):
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Kazandın!")
          sona()
        elif sum(pc) > sum(ben):
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Kaybettin!")
          sona()
        else:
          print(f"Senin elin: {ben}, Senin skorun: {sum(ben)}\nBilgisayarın eli: {pc}, Bilgisayarın skoru: {sum(pc)}")
          print("Berabere.")
          sona()
  fonksiyon()



##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

