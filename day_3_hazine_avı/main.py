print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine avına hoş geldin.")
print("Görevin hazineyi bulmak.\n")

print("Hava karanlık, yollar loş sokak ışıklarıyla aydınlatılmış. \n Yol ayrımına geliyorsun. Sağ tarafta kocaman bir dağın siluetini görüyorsun. Solda ise Yol gittikçe alçalarak bir kanyona giriyor. \n Hangi yolu seçiyorsun?")
yol_ayrımı = input("sağ - sol \n ")
if yol_ayrımı == "sağ":
  print("Dağın eteklerine doğru yola çıktın. Eğimli bir arazide hızla yol alırken soldaki ormanlıktan maymun sesleri gelmeye başlıyor. Ses geldiği anda o tarafa bakıyorsun ve sana doğru koşan bir maymun var. Kendini koruman gerek. Ne kullanacaksın?")
  maymun_geliyor = input("ok ve yay - bıçak - kaç \n")
  if maymun_geliyor == "ok ve yay":
    print("Maymun sana doğru koşarken gözünü ayırmadan ok yayını çıkarıp geriyorsun. Sen tetikte doğru anı beklerken maymun bir anda küçük bir sazlığa giriyor ve onu gözden kaybediyorsun. Bir anda arkandan gelen bir maymun sesinden sonrası yok. OYUN BİTTİ. TEKRAR DENE.")
  elif maymun_geliyor == "bıçak":
    print("Maymun sana doğru koşarken gözünü ayırmadan bıçağını çıkarıyorsun. Maymun küçük bir sazlığa giriyor ve onu gözden kaybediyorsun. Bir anda arkandan gelen bir maymun sesiyle arkanı dönüp maymuna delici bir hamle yapıyorsun. Sen neye uğradığı tam idrak edemeden ortalıkta ölü maymundan başka bir şey kalmıyor. \n Yoluna hızla devam ediyorsun. Artık eğim iyice dikleşti birkaç saat tırmandıktan sonra önünde çok büyük bir mağarayla karşılaşıyorsun. Mağaraya mı gireceksin, yoksa hazine dağın tepesinde mi")
    dağ_mağara = input("dağ - mağara\n")
    if dağ_mağara == "dağ":
      print("Dağ iyice dikleşti. Yanında dağcılık ekipmanı olmadığı halde dik kayalıklara tırmanmaya devam ediyorsun. Riskli bir yeri geçerken ayağın kayıyor. OYUN BİTTİ. TEKRAR DENE.")
    elif dağ_mağara == "mağara":
      print("Mağara şu ana kadar gördüğün en büyüğü. İçerisi gittikçe serinliyor fakat yine de elinde el feneriyle 1 saat boyunca ilerliyorsun. Meydan gibi büyük bir kısma geldiğinde fenerin tahta bir şeye takılıyor. HAZİNE! OYUN BİTTİ.")
  elif maymun_geliyor == "kaç":
    print("Hızla koşuyorsun fakat bu maymun kudurmuş. Gözü dönmüş maymun hızla seni yakalıyor ve yemeye başlıyor. \n OYUN BİTTİ. TEKRAR DENE.")
if yol_ayrımı == "sol":
  print("Kanyon gittikçe derinleşiyor. Artık sağında ve solunda kayalar 50m den fazla. Uzun bir yoldan sonra patikanın sağ tarafında bir yapı dikkatini çekiyor. Demir parmaklıklar var ama, burası bir hapishane olacak kadar büyük değil. Giriyor musun?")
  hapishane = input("gir - yola devam\n")
  if hapishane == "yola devam":
    print("Yapıyı geçip yola devam ediyorsun. Kanyonun içindeki patika gittikçe darlaşıyor ve en sonunda büyük bir mağara var, fakat bu mağara içine girebilmek için çok derin. OYUN BİTTİ. TEKRAR DENE.")
  elif hapishane == "gir":
    print("Parmaklıklar artık çürümüş. Birkaç vuruşa açılıyorlar. İçerisi zifiri karanlık. Fenerini çıkarıyorsun. Burada büyükçe bir koridor var. Sonuna kadar gidiyorsun. Koridorun sonunda 3 tane oda var. Hangisine giriyorsun?")
    oda = input("1 - 2 - 3\n")
    if oda == "1" or "2" or "3":
      print("Oda boş. OYUN BİTTİ. TEKRAR DENE.")