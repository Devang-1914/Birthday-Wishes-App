import datetime as dt
import smtplib
import pandas as pd
import random

MY_EMAIL = "YOUR_EMAIL_ADDRESS"
PASSWORD = "EMAIL_PASSWORD"


#----------------------- Check if today matches a birthday in the birthdays.csv -------------------#

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)


#------------------------- read the birthdays.csv --------------------------------------#
data = pd.read_csv("birthdays.csv")

#------------------------------ Creating Dictionary form Birthday.csv ----------------------------#

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#------------------ Comparing and checking if today's month/day tuple matches one of the keys in birthday_dict ---------------------------#

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


#--------------------- Emailing the letter generated above to that person's email address -------------------#
# Various sources  Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")



