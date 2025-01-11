#import logo and print it
#get 2 data, one becomes A and other B
#compare their follower
#if wrong, end game
#if right, previous B becomes A, and get a new B.
import os
import random
from game_data import data
from art import logo, vs

random.choice(data)

skor = 0
print(logo)

data1 = random.choice(data)


def oyna(skor):
  global data1
  data2 = random.choice(data)
  if data1 == data2:
    data2 = random.choice(data)

  if data1['follower_count'] > data2['follower_count']:
    winner = data1
  else:
    winner = data2

  print(f"Skorun {skor}\nİnstagramda kimin daha fazla takipçisi var?")
  print(
      f"A : {data1['name']}, {data1['description']}, from {data1['country']}")

  print(vs)

  print(
      f"B : {data2['name']}, {data2['description']}, from {data2['country']}")

  tahmin = input("A ya da B yaz: ")
  if tahmin == "A" and winner == data1 or tahmin == "B" and winner == data2:
    skor += 1
    data1 = data2
    os.system('clear')
    oyna(skor)
  else:
    print(f"Yanlış bildin. Skorun {skor}.")

oyna(skor)
