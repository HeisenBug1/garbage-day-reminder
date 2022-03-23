import datetime
import os
import sys
import re


def read_first_run():
	print("Initial setup started...\n")
	print("When was your last garbage day?")
	while True:
		day = input('Type "Today", "Tomorrow", "Yesterday" or MM-DD (Month-Day)\nEnter: ')
		day = day.lower()
		# if day == 'today':
		# 	break
		# elif day == 'tomorrow':
		# 	break
		# elif day == 'yesterday':
		# 	break
		# elif 
		match = re.search("[0-1][0-2]-[0-3][0-9]", day)
		break


	print(match)

read_first_run()
