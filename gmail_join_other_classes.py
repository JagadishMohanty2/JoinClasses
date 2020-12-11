from selenium import webdriver
import traceback

from selenium.webdriver.chrome.options import Options
import time
import os

import sys
from selenium.webdriver.common.action_chains import ActionChains
# to type `stuff etc`, press entere etc
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait

# Loads chrome with default settings
opt = Options()
opt.add_argument("start-maximized")  # maximising the screen
opt.add_argument("--disable-extensions")  # not allowing extensions to load up

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# PATH = "C:\\Users\\devi\\Desktop\\Rahul\\PythonCoding\\Learn\\Python\Selenium__\\msedgeself.driver_older.exe"

# # Gives path to chrome WebDriverWait.driver and loads classroom webpage
# driver = WebDriverWait.driver.Edge(PATH)
# driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')


class Main:
    def __init__(self):
        '''initializes varaibles and opens up the browser'''

        self.PATH = "C:\\Users\\devi\Desktop\\Rahul\PythonCoding\\Learn\Python\Selenium__\\msedgedriver_older.exe"

        self.driver = webdriver.Edge(self.PATH)

        # Gives path to chrome WebDriverWait.driver and loads classroom webpage
        self.driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

    def log_into_gmail(self):
        '''logs into my gmail account'''
        try:
            # giving the email
            email_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )

            email_input.send_keys(os.environ.get("gmail_email"))
            self.driver.find_element_by_id("identifierNext").click()

        except Exception as err:
            traceback.print_exc()

        try:
            time.sleep(5)
            # giving the password
            password_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            password_input.send_keys(os.environ.get("gmail_pass"))

            # clicking sign in
            self.driver.find_element_by_id("passwordNext").click()

        except Exception as err:
            traceback.print_exc()

        else:
            return self.which_class()

    def which_class(self):
        '''Finds out what class i have and joins it'''

        localtime = time.localtime()
        time_now = f"{localtime.tm_hour}:{localtime.tm_min}"
        # to tind out what day it is
        day = datetime.datetime.now().strftime("%A")
        self.class_time = 40*60

        if day == "Monday":
            # bot would join 5 mins early
            self.join_Eng()

            # double maths
            self.join_Math()
            self.join_Math()

            # break
            time.sleep(30*60)

            # double accounting
            self.join_Acc()
            self.join_Acc()

            # break
            time.sleep(30*60)

            # spanish
            self.join_Spanish()

            # physics
            self.join_Physics()

        if day == "Tuesday":
            # chemistry
            self.join_Chem()

            # double English
            self.join_Eng()
            self.join_Eng()

            # spanish
            self.join_Spanish()

            # break
            time.sleep(30*60)

            # double computer science
            self.join_Comp()
            self.join_Comp()

            # double physics
            self.join_Physics()
            self.join_Physics()

        if day == "Wednesday":
            # english
            self.join_Eng()

            # accounting
            self.join_Acc()

            # physics
            self.join_Physics()

            # computer science
            self.join_Comp()

            # break
            time.sleep(30*60)

            # maths
            self.join_Math()

            # spanish
            self.join_Spanish()

            # break
            time.sleep(30*60)

            # double chemistry
            self.join_Chem()
            self.join_Chem()

            exit(code="School Over")

        if day == "Thursday":
            # accounting
            self.join_Acc()

            # chemistry
            self.join_Chem()

            # maths
            self.join_Math()

            # computer science
            self.join_Comp()

            # break
            time.sleep(30*60)

            # physics
            self.join_Physics()

            # english
            self.join_Eng()

            # break
            time.sleep(30 * 60)

            # spanish
            self.join_Spanish()

            # english
            self.join_Eng()

        exit(code="School Over")

    def join_class_room(self, class_number):
        '''finds the classroom and clicks it'''

        # Finds the classroom   asscesing CS
        classroom = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'YVvGBb csjh4b')]"))
        )[class_number]

        classroom.click()

    def join_meet_switch_tabs(self):
        '''goes to the next tab, and joins the meet'''

        # Switches the tab
        # self.driver.switch_to.window(self.driver.window_handles[1])
        try:
            current_tab = self.driver.window_handles[1]
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as err:
            pass

        time.sleep(10)
        return self.join_meet()

    def join_Comp(self):
        '''joins my Computer Science class room'''

        self.join_class_room(1)

        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/gtsn2d5uvg"))
        )

        link.click()

        # time.sleep(45*60)
        return self.join_meet_switch_tabs()

    def join_Eng(self):
        '''joins my English classroom'''

        self.join_class_room(4)
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/hdo7g4uwfi"))
        )

        link.click()

        # time.sleep(45*60)
        return self.join_meet_switch_tabs()

    def join_Chem(self):
        '''joins my Chemistry classroom'''

        self.join_class_room(3)
        
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/bf6lbncayn"))
        )

        link.click()

        return self.join_meet_switch_tabs()

    def join_Acc(self):
        '''joins my Accoutning class'''

        time.sleep(45*60)
        return

    def join_Math(self):
        '''joins my Math class'''

        time.sleep(45*60)
        return

    def join_Physics(self):
        '''joins my Physics class'''

        time.sleep(45*60)
        return

    def join_Spanish(self):
        '''joins my Spanish class'''

        time.sleep(45*60)
        return

    def join_meet(self):
        '''turns of mic, camera, and joins the meet'''

        turn_off_mic_action = ActionChains(self.driver)
        #                               ctrl + d --> turns of mic
        turn_off_mic_action.key_down(Keys.CONTROL).send_keys(
            "d").key_up(Keys.CONTROL).perform()

        # turns of my camera
        turn_off_camera_action = ActionChains(self.driver)
        #                               ctrl + e --> turns of camera
        turn_off_camera_action.key_down(Keys.CONTROL).send_keys(
            "e").key_up(Keys.CONTROL).perform()

        # joining the meet
        join = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Join now')]"))
        )
        join.click()

        print("Joined")
        time.sleep(60*45) # change it to 45*60
        return self.leave_call()

    def leave_call(self):
        '''leaves the meet'''

        self.driver.close()
        
        try:
            current_tab = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as err:
            pass
        
        print("Left")

        # goes back a page
        self.driver.back()
        return


Main().log_into_gmail()
# line 82 to change what class to join
