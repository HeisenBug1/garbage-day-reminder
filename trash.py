import datetime, pickle


# if running script for the first time
# gather all necessary data
def first_run():
	import sys, re	# RegEx

	print("Initial setup started...\n")
	print("When was your last garbage day?")
	if sys.stdout.isatty() is True:
		while True:
			while True:
				day = input('Type "Today", "Tomorrow", "Yesterday" or MM-DD (Month-Day)\nEnter: ').lower()
				match = re.search("^([0][1-9]|[1][0-2])-([0][1-9]|[1-2][0-9]|[3][0-1])$", day)
				
				if'tod' in day:
					day = datetime.date.today()
					break
				elif 'tom' in day:
					day = datetime.date.today() + datetime.timedelta(days=1)
					break
				elif 'yes' in day:
					day = datetime.date.today() - datetime.timedelta(days=1)
					break
				elif match is not None:
					day = day.split("-")
					day[0] = int(day[0])
					day[1] = int(day[1])
					day = datetime.date(int(datetime.date.today().strftime("%Y")), day[0], day[1])
					break
				else:
					print("\tWrong entry: "+day+"\n\tPlease try again\n")

			if 'y' in input("Is "+day.strftime("%A, %b-%d")+" correct? (yes/no) ").lower():
				break
			else:
				print("\tThen please try again\n")

		while True:		
			garbage_type = input("Was it Recycle Only? or both Recycle & Waste?\nType 'waste' or 'both': ").lower()
			if 'both' in garbage_type:
				garbage_type = 'Both Recycle & Waste'
				break
			elif 'was' in garbage_type:
				garbage_type = 'Waste Only'
				break
			else:
				print("\tWrong entry: "+garbage_type+"\n\tPlease try again\n")

		sender = input('Send email notifications from?: ')
		password = input('Password: ')
		receiver = input('Recipient: ')

		return {
			"day": day,
			"type": garbage_type,
			"sender": sender,
			"password": password,
			"receiver": receiver 
			}
	else:
		print('Interactive shell not found')
		return None


# check if data exists
def initialize():
	try:
		with open('trash_data.pkl', 'rb') as file:
			return pickle.load(file)
	except:
		print('No datafile found')
		return first_run()


# notify user about current email
def send_email(data):
	import smtplib, ssl

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = data['sender']  # Enter your address
	receiver_email = data['receiver']  # Enter receiver address
	password = data['password']
	msg = data['type']
	if 'Subject:' in msg:
		message = msg
	else:
		message = "Subject: Garbage Notification\n\n"+msg

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)


print()
