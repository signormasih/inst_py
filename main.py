from src.fileReader import *
import os

dir_name = os.path.dirname(os.path.realpath(__file__))

banner = '''
	[[ INSTAGRAM BRUTE-FORCE ]]
'''
print(banner)

if os.path.exists(f"{dir_name}/report/done.txt"):
	os.remove(f"{dir_name}/report/done.txt")
if os.path.exists(f"{dir_name}/report/maybe_two_step.txt"):
	os.remove(f"{dir_name}/report/maybe_two_step.txt")

username = str(input('Username (Combolist -> using ./catch/username_list.txt) : '))
r_d = ReadData(dir_name,username)

if username:
	r_d.read_data()
else:
	r_d.read_data_combo()


