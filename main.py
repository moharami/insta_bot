from insta import Instagram
import os

driver_path = "C:\\chromedriver.exe"
email = "g.s.travel.agency"
password = "Ghasedak388"

insta = Instagram(webdriver_path=driver_path, email=email, pass_=password)
insta.login()

# Searching a specific account with similiar content like mine and following the people who
# who follows that account
# insta.search_accounts(account_username="asemanehaftom_agency")
# insta.followerpage(account_username="asemanehaftom_agency")

# insta.follow("matin.mira")
insta.like_post("canpars")

# # unfollow every one
# insta.unfollow()

insta.close_window()