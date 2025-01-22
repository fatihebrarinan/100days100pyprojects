import pandas
import smtplib
import datetime
import random

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
df = pandas.read_csv("birthdays.csv")
letter_list = []

user = "ap9872355@gmail.com"
password = "sample_password"
connection =  smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=user, password=password)

for index, row in df.iterrows():
    if row['month'] == now.month and row['day'] == now.day:
        letter_list.append(open("letter_templates/letter_1.txt", "r"))
        letter_list.append(open("letter_templates/letter_2.txt", "r"))
        letter_list.append(open("letter_templates/letter_3.txt", "r"))

        random_letter = random.choice(letter_list)
        message = random_letter.read().replace("[NAME]", row['name'])

        connection.sendmail(
            from_addr=user,
            to_addrs=row['email'],
            msg=f"Subject: Happy Birthday!\n\n{message}"
        )

connection.close()
for _ in letter_list:
    _.close()










# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




