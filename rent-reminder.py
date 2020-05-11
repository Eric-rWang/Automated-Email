import csv
import smtplib
from email.message import EmailMessage


email, password = input('Email, Password: ').split()
contactList = input('Email csv file: ')
contacts = []

# csv file has to have first space left blank
with open(contactList) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_file:
		contacts.append(row)

contacts = contacts[1:]

# establishing secure connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	# login
	smtp.login(email, password)

	# send email to each contact listed in list
	for i in contacts:
		# constructing message
		msg = EmailMessage()
		msg['Subject'] = 'Monthly Rent Reminder!'
		msg['From'] = email
		msg['To'] = i
		msg.set_content('Just a friendly reminder that this months rent is due tomorrow. Please reach out with any questions or concerns. \n\nThanks,\nEric Wang')
		
		smtp.send_message(msg)

