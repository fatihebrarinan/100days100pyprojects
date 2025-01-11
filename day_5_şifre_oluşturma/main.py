#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre oluşturma programına hoş geldin!")
nr_letters = int(input("Şifrende kaç harf istiyorsun?\n"))
nr_symbols = int(input(f"Şifrende kaç sembol istiyorsun?\n"))
nr_numbers = int(input(f"Şifrende kaç rakam istiyorsun?\n"))
a = ""
for i in range(0,nr_letters):
  rastgele_harfler = random.randint(0,len(letters)-1)
  a += letters[rastgele_harfler]
b = ""
for i in range(0,nr_symbols):
  rastgele_semboller = random.randint(0,len(symbols)-1)
  b += symbols[rastgele_semboller]
c = ""
for i in range(0,nr_numbers):
  rastgele_sayılar = random.randint(0,len(numbers)-1)
  c += numbers[rastgele_sayılar]
s = a + b + c
a = list(s)
random.shuffle(a)
s = "".join(a)
print(f"Şifreniz: {s}")