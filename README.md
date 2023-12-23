***Don't forget to put a star***




# gmail-hack
Hello. All Two programs are used to extract emails stored on a Windows system and send them to yourself using one of the same extracted emails. You can use a memory with automatic execution or manually execute on the target. Note that combining these 2 codes is your responsibility.


***Extraction.py***
This code connects to the Outlook application using the ``win32com.client'' library and collects the information of the email accounts in Outlook. It then stores this information (email addresses and passwords) in a text file named "email_accounts.txt".

***get_backup.py***
This code is read from the email account information collected in the first code. Then it creates a backup file of emails and sends it to a desired email address. This code uses the SMTP protocol to send email.

*****@pouryet*****
