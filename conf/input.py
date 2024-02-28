class Payload:
	def __init__(self, username, password, time):
		self.username = f'{username}'
		self.enc_password = f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}'  # <- note the '0' - that means we want to use plain passwords
		self.queryParams = {}
		self.optIntoOneTap = 'false'
		
