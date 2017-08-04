#!/bin/python3

import datetime, threading, winsound
from time import sleep

class alarm(threading.Thread):
	def __init__(self, time, nom):
		self.time = time
		self.nom = nom
		threading.Thread.__init__(self)
		self.start()

	def run(self):
		while 1:
			sleep(5)
			now = datetime.datetime.now()
			if str(now.year)[-2:] == self.time[0:2] and int(now.month) == int(self.time[3:5]) and int(now.day) == int(self.time[6:8]):
				if int(now.hour) == int(self.time[9:11]) and int(now.minute) == int(self.time[12:14]):
					print("\n\nAlarm went off!\n" + self.nom + "\n\nWhat would you like to do? ('help' for help)")
					break

class timer(threading.Thread):
	def __init__(self, time, nom):
		self.time = int(time)
		self.nom = str(nom)
		threading.Thread.__init__(self)
		self.start()

	def run(self):
		sleep(int(self.time))
		print("\n\nTimer went off!\n" + self.nom + "\n\nWhat would you like to do? ('help' for help)")

def Main():
	#with open("alarms.txt", "w+") as f: f.close()
	while 1:
		uin = input("\nWhat would you like to do? ('help' for help)\n")
		if uin == 'help':
			print("new alarm <name> <time (YY/MM/DD/hh/mm)> - makes a new alarm\nnew timer <name> <time (tttttttt)> - makes a new timer (seconds)\nhelp - shows this\nquit - exit the program")
		elif uin[0:9] == 'new alarm':
			alarm(str(uin)[-14:], str(uin)[10:-14])
			print("Alarm made.")
		elif uin[0:9] == 'new timer':
			timer(int(str(uin[-8:])), str(uin[10:-8]))
			print("Timer made.")
		elif uin[0:4]:
			quit()
		else:
			print("Command not found.")

if __name__ == '__main__':
	Main()