from insta import Instagram
from text import Text
from decouple import config
import os

driver_path = "C:\\chromedriver.exe"


email = config('email')
password = config('password')


file_name = './data/' + config('email') + '/to_follow.txt'


insta = Instagram(webdriver_path=driver_path, email=email, pass_=password)
insta.login()




for x in range(1):
	account = Text.readfirst(file = file_name)
	print(account)

	# insta.like_post(account)
	insta.follow(account)

	print(account)
	Text.deletefirst(file = file_name)

insta.close_window()