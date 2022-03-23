import datetime
import os
import sys
import re


def first_run():
	print("Initial setup started...\n")
	print("When was your last garbage day?")
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

first_run()
