import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9,tr;q=0.8",
}
response = requests.get("https://kupsepeti.com/products/yj-mgc-6x6", headers=header)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="price-item price-item--sale price-item--last").getText().strip()
price = float(price[:-1].split(",")[0]) * 1000
email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")

connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)

if price < 2000:
    connection.sendmail(from_addr=email,
                    to_addrs=email,
                    msg=f"Subject:Amazon Price Alert!\n\n6x6 cube price dropped to {price}TL!\n".encode("utf-8"))