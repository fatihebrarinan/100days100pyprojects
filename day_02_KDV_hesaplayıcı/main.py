print("İNAN MOBİLYA mağazasının vergi hesaplayıcısına hoş geldiniz.")
fiyat = input("Aldığınız ürünün vergisiz fiyatını yazınız. ₺")
taksit = input("Ürünü kaç taksitle aldığınızı yazınız. ")

KDV_fiyat = float(fiyat) * 1.2
KDV_taksit = KDV_fiyat / int(taksit)

print(f"Ürününüzün KDV'li fiyatı {KDV_fiyat}₺ dir.")
print(f"Ürününüzün bir taksidinin KDV'li fiyatı {KDV_taksit}₺ dir.")