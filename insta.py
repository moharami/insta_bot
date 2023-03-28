from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from decouple import config

class Instagram:
    def __init__(self, webdriver_path, email, pass_):
        '''Takes three required params wedriver_path:type(str),
        email:type(str),pass_:type(str)'''

        self.people_followed = 0
        self.webdriver_path = webdriver_path
        self.email = email
        self.pass_ = pass_
        self.driver = webdriver.Chrome(executable_path = self.webdriver_path)
    
    def login(self):
        '''This function logs you in to the instagram'''

        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

        self.driver.find_element(By.NAME, "username").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.pass_)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
        time.sleep(15)
    
    def search_accounts(self, account_username):
        '''Takes one required argument account_username:type(str)
        to find and open the profile of the username mentioned in
        parameter'''

        time.sleep(3)
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div').click()
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div')
        time.sleep(5)
        search_box.send_keys(account_username)
        time.sleep(5)
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)

    def scroll_and_follow(self, scroll_limit):
        '''Takes one required parameter scroll_limit:type(int)
        Its is recommend to pass maximum value of 125'''

        time.sleep(3)
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)

        for _ in range(scroll_limit):
            time.sleep(2)
            scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        buttons = self.driver.find_elements_by_class_name("sqdOP")
        for button in buttons:
            time.sleep(1)
            if button.text == "Follow":
                # button.click()
                self.people_followed += 1
            else:
                pass
    
    def unfollow(self):
        '''This function unfollows everyone you are following'''

        time.sleep(3)
        self.driver.find_element_by_class_name("_6q-tv").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("-qQT3").click()

        time.sleep(3)
        user_info = self.driver.find_elements_by_class_name("-nal3")
        user_info[2].click()

        # Scroll through following list 
        for _ in range(5):
            time.sleep(2)
            scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        # Unfollow people one by one
        time.sleep(2)
        buttons = self.driver.find_elements_by_class_name("sqdOP")
        for button in buttons:
            if button.text == "Following":
                button.click()
                time.sleep(3)
                unfollow_btn = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]")
                unfollow_btn.click()
                time.sleep(3)
            
    def close_window(self):
        time.sleep(5)
        self.driver.quit()

    def follow(self, username):
        try:
            self.driver.get("https://www.instagram.com/" + username)
            time.sleep(int(config('wait_before_each_follow')))
            # followbtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button')
            # followbtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            followbtn = self.driver.find_element(By.XPATH, "//*[text()='Follow']")
            followbtn.click()
            time.sleep(5)
        except:
            print("we cant follow account = "+ username)
        



    def like_post(self, username):

        try:
            self.driver.get("https://www.instagram.com/" + username)
            time.sleep(10)
    
            # first_post = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')
            second_post = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a')
            second_post.click()

            time.sleep(7)

            for x in range(int(config('count_like_post'))):
                like_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
                like_button.click()
                time.sleep(2)
                # next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                next_button.click()
                time.sleep(3)
        except:
            print("we cant like post for account = " + username)
            
        



