import datetime as dt
import random
import smtplib
import pandas


if __name__ == "__main__":
    PATH_BIRTHDAYS = "./birthdays.csv"

    MY_EMAIL = ""
    MY_PASSWORD = ""

    SMTP_GMAIL = "smtp.gmail.com"
    SMTP_YAHOO = "smtp.mail.yahoo.com"

    PORT = 587

    today = (dt.datetime.now().month, dt.datetime.now().day)
    data = pandas.read_csv(PATH_BIRTHDAYS).to_dict(orient="Records")

    for row in data:
        if today == (row["month"], row["day"]):
            path_letter = f"./letters/letter_{random.randint(1, 3)}.txt"
            name = row["name"]
            email = row["email"]

            with open(path_letter) as letter:
                msg_subject = "Happy Birthday!"
                msg_body = letter.read().replace("[NAME]", f"{name}")
                msg = f"Subject:{msg_subject}\n\n{msg_body}"

            with smtplib.SMTP(SMTP_GMAIL, port=PORT) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=msg)

                print(f"Birthday letter sent to {row['name']}")
