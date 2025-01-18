import smtplib
import datetime as dt
import random

user = "ap9872355@gmail.com"
password = "uwgcaisvnfhqdfgt"
connection =  smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=user, password=password)

quote_file = open("quotes.txt", "r")
quote_list = quote_file.readlines()

now =  dt.datetime.now()
if now.weekday() == 3:
        connection.sendmail(
            from_addr=user,
            to_addrs="fatihebrarinan@gmail.com",
            msg=f"Subject:You can do it.\n\n{random.choice(quote_list)}"
        )
connection.close()
quote_file.close()

